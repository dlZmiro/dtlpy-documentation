## Pipelines

Dataloop’s pipeline system integrates human and machine processing in a series of interconnected nodes to streamline data handling. The pipeline architecture allows for data to flow through labeling tasks, quality assurance tasks, functions within the Dataloop system, code snippets, and machine learning models, allowing for data filtering, splitting, merging, and status changes as needed.

With Dataloop’s pipeline, organizations can streamline any production pipeline, preprocess and label data, automate operations with applications and models, and postprocess data for training machine learning models at optimal performance and availability standards.

As an example, a pipeline may start with preprocessing data through code snippets (such as cutting a video into frames), then sending the output to multiple parallel tasks for labeling, quality assurance, or other processes. Completed tasks can then be directed to a separate task for review, while discarded items are stored in a separate dataset.

## Pipelines in SDK
The Dataloop platform allows for the manipulation and use of pipelines through both the user interface and the software development kit (SDK). For the purpose of this section, we will focus on working with pipelines through the SDK, but we will also provide additional resources at the end in the form of video tutorials for those who prefer to use the web version of Dataloop for managing pipelines.

First, let's create a new pipeline:
```python

pipeline = project.pipelines.create(name='My-First-Pipeline')

```
You have now defined a new pipeline called "My-First-Pipeline". To see the details of this new pipeline, you can simply print them:

```python
print(pipeline)
```
After doing so, you should see some details similar to this:
```python
Pipeline(id='63d93916845ca8a3f161d5fc', name='My-First-Pipeline', creator='email@gmail.com', org_id='8c8387a3-e771-4d2b-ad77-6a30294dbd01', connections=[], settings=<dtlpy.entities.pipeline.PipelineSettings object at 0x000002BB46FD36D0>, status='Created', created_at='2023-01-31T15:51:50.837Z', start_nodes=[], project_id='764803e6-af9b-4dde-8141-fea54231fb54', composition_id='63d93916845ca883da61d5fd', url='https://gate.dataloop.ai/api/v1/pipelines/63d93916845ca8a3f161d5fc', preview=None, description=None, revisions=None)
```
Now, you can take the id you got by printing the details of your pipeline, and use it in the following line of code, to "get" your pipeline:

```python
pipeline = project.pipelines.get(pipeline_id='pipeline_id')
```
Next, you will use a line of code which will execute the pipline and return an object in the "pipeline_execution" variable we create:
```python
pipeline_execution= project.pipelines.execute(pipeline='pipeline_entity', execution_input= {'item': 'item_id'} )
```
To get the item id for a sample, dataset or pipeline, you can simply print it, like this:
```python
print(item_1)
```
In the example above, you print the details of a sample you defined in a previous chapter, which you also should have defined if you followed and coded along the way. Here is how the output should look like (with different id and other details):
```python
Item(dataset_url='https://gate.dataloop.ai/api/v1/datasets/63cebc185bc9dbe3ed851dbe', created_at='2023-01-23T17:04:15.000Z', dataset_id='63cebc185bc9dbe3ed851dbe', filename='/test1.jpg', name='test1.jpg', type='file', id='63cebe0f6f60196b004423d9', spec=None, creator='myfuncont@gmail.com', _description=None, annotations_count=3)
```
Now you should have all the information to execute your pipeline. Here are also some other useful lines of code, that will help you when working with pipelines in the SDK.

1. Delete a pipeline object:
```python
is_deleted = project.pipelines.delete(pipeline_id='pipeline_id')
```
2. List all pipelines:
```python
project.pipelines.list()
```
3. Open pipelines in web view:
```python
project.pipelines.open_in_web(pipeline_id='pipeline_id')
```
4. Pause the pipeline process:
```python
project.pipelines.pause(pipeline='pipeline_entity')
```
5. Reset pipeline:
```python
project.pipelines.reset(pipeline='pipeline_entity')
```
6. Get a pipeline's stats:
```python
project.pipelines.stats(pipeline='pipeline_entity')
```
7. Execute pipeline and return the execute in a variable:
```python
pipeline_execution = pipeline.pipeline_executions.create(pipeline_id='pipeline_id', execution_input={'item': 'item_id'})
```
8. Get pipeline execution object:
```python
pipeline_executions = pipeline.pipeline_executions.get(pipeline_id='pipeline_id')
```
9. List project pipeline executions objects:
```python
pipeline.pipeline_executions.list()
```
If you want to find out more about all of these commands, including descriptions of each parameters they take as input, <a href="https://dlportal-demo.redoc.ly/resources/dtlpy/dl/#:~:text=Pipelines-,class%20Pipelines(client_api%3A%20ApiClient%2C%20project%3A%20Optional%5BProject%5D%20%3D%20None),-Bases%3A">read more here</a>.
## Creating pipelines in UI

If you are interested in how you can work with pipelines in the web version of dataloop, here are some video tutorials to get you started:

1. [Simple pipeline](https://app.guidde.co/share/playbooks/p88yeiCCZYPJ5De92KRhNz?origin=jMK1qNxyBfeCaSgiUvBzFi9AfJb2)
2. [Task to task pipeline](https://app.guidde.co/share/playbooks/d4VKpz2wXkEfC3b8KtScoj?origin=jMK1qNxyBfeCaSgiUvBzFi9AfJb2)
3. [Task with FAAS and Filter](https://app.guidde.co/share/playbooks/uhQbzYGjMZjQoAWGMzcM3r?origin=jMK1qNxyBfeCaSgiUvBzFi9AfJb2)
4. [Task with Filter](https://app.guidde.co/share/playbooks/f94hGsB1CoURVjVUhD354B?origin=jMK1qNxyBfeCaSgiUvBzFi9AfJb2)

In the next chapter you will learn about model management which will help you to understand in depth the full cycle that you can implement into your workflows using Dataloop.
