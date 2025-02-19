import dtlpy as dl


def func1():
    import dtlpy as dl
    import os
    project = dl.projects.get(project_name='<project_id>')
    package = project.packages.push(package_name='dummy-model-package',
                                    codebase=dl.entities.LocalCodebase(os.getcwd()),
                                    modules=[])
    model = package.models.create(model_name='My Model',
                                  description='model for offline model logging',
                                  dataset_id='<dataset_id>',
                                  labels=[])


def func2():
    epoch = np.linspace(0, 9, 10)
    epoch_metric = np.linspace(0, 9, 10)

    for x_metric, y_metric in zip(epoch, epoch_metric):
        model.add_log_samples(samples=dl.LogSample(figure='tutorial plot',
                                                   legend='some metric',
                                                   x=x_metric,
                                                   y=y_metric),
                              dataset_id=model.dataset_id)

