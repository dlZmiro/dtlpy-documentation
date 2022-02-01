def func1():
    import dtlpy as dl
    import cv2

    import numpy as np

    class ImageProcess(dl.BaseServiceRunner):
        @staticmethod
        def rgb2gray(item: dl.Item):
            """
            Function to convert RGB image to GRAY
            Will also add a modality to the original item
            :param item: dl.Item to convert
            :return: None
            """
            buffer = item.download(save_locally=False)
            bgr = cv2.imdecode(np.frombuffer(buffer.read(), np.uint8), -1)
            gray = cv2.cvtColor(bgr, cv2.COLOR_BGR2GRAY)
            gray_item = item.dataset.items.upload(local_path=gray,
                                                  remote_path='/gray' + item.dir,
                                                  remote_name=item.filename)
            # add modality
            item.modalities.create(name='gray',
                                   ref=gray_item.id)
            item.update(system_metadata=True)

        @staticmethod
        def clahe_equalization(item: dl.Item):
            """
            Function to perform histogram equalization (CLAHE)
            Will add a modality to the original item
            Based on opencv https://docs.opencv.org/4.x/d5/daf/tutorial_py_histogram_equalization.html
            :param item: dl.Item to convert
            :return: None
            """
            buffer = item.download(save_locally=False)
            bgr = cv2.imdecode(np.frombuffer(buffer.read(), np.uint8), -1)
            # create a CLAHE object (Arguments are optional).
            lab = cv2.cvtColor(bgr, cv2.COLOR_BGR2LAB)
            lab_planes = cv2.split(lab)
            clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
            lab_planes[0] = clahe.apply(lab_planes[0])
            lab = cv2.merge(lab_planes)
            bgr_equalized = cv2.cvtColor(lab, cv2.COLOR_LAB2BGR)
            bgr_equalized_item = item.dataset.items.upload(local_path=bgr_equalized,
                                                           remote_path='/equ' + item.dir,
                                                           remote_name=item.filename)
            # add modality
            item.modalities.create(name='equ',
                                   ref=bgr_equalized_item.id)
            item.update(system_metadata=True)


def func2():
    import dtlpy as dl

    modules = [dl.PackageModule(name='image-processing-module',
                                entry_point='main.py',
                                class_name='ImageProcess',
                                functions=[dl.PackageFunction(name='rgb2gray',
                                                              description='Converting RGN to gray',
                                                              inputs=[dl.FunctionIO(type=dl.PackageInputType.ITEM,
                                                                                    name='item')]),
                                           dl.PackageFunction(name='clahe_equalization',
                                                              description='CLAHE histogram equalization',
                                                              inputs=[dl.FunctionIO(type=dl.PackageInputType.ITEM,
                                                                                    name='item')])
                                           ])]


def func3():
    project_name = 'MyProject'
    src_path = 'functions/opencv_functions'
    project = dl.projects.get(project_name=project_name)
    package = project.packages.push(package_name='image-processing',
                                    modules=modules,
                                    src_path=src_path)


def func4():
    service = package.services.deploy(service_name='image-processing',
                                      runtime=dl.KubernetesRuntime(concurrency=32),
                                      module_name='image-processing-module')


def func5():
    trigger = service.triggers.create(name='image-processing',
                                      execution_mode=dl.TriggerExecutionMode.ONCE,
                                      resource=dl.TriggerResource.ITEM,
                                      actions=dl.TriggerAction.CREATED,
                                      filters=dl.Filters(field='dir', values='/incoming'))


def func6():
    execution = service.execute(execution_input=[dl.FunctionIO(type=dl.PackageInputType.ITEM,
                                                               name='item',
                                                               value='<item_id>')])
    execution = execution.wait()
    print(execution.status)


def func7():
    execution.logs()


def func8():
    slots = [
        dl.PackageSlot(
            module_name='image-processing',
            function_name='rgb2gray',
            display_name='RGB2GRAY',
            post_action=dl.SlotPostAction(type=dl.SlotPostActionType.NO_ACTION),
            display_scopes=[
                dl.SlotDisplayScope(
                    resource=dl.SlotDisplayScopeResource.ITEM,
                    filters={}
                )
            ]
        ),
    ]
    package.slots = slots
    package.update()
    service.package_revision = package.version
    service.update()
