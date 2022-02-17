## Intro

TODO: describe functions that are too big, show an example

describe the very basic concept of refactoring (we will have a whole module on this later, but here's an initial taste)

## Activity

Here is some code that's too big:

The code below is taking in a dictionary and a list of operations that needs to be done to the list that is passed in. The code passes in a dictionary, dict with key value pairs that represent a person and their current job. 

```
def jobScheduling(peoples_job, operations, operating_person, operating_result):
    counter = 0
    jobs_changed = 0
    jobs_added = 0
    jobs_removed = 0
    for x in operations:
        if x == 'change':
            peoples_job.get(operating_person.get(counter)) == operating_result.get(counter)
            jobs_changed += 1
        elif x == 'add':
            peoples_job.put(operating_person.get(counter), operating_result.get(counter))
            jobs_added += 1
        elif x == 'remove':
            peoples_job.get(operating_person.get(counter)) == 'unemployed'
            jobs_removed += 1
    if jobs_changed > jobs_added:
        if jobs_changed > jobs_removed:
            print('Most jobs were changed')
        else:
            print('Most jobs were removed')
    else:
        if jobs_added > jobs_removed:
            print('Most jobs were added')
        else:
            print('Most jobs were removed')
        return peoples_job

```
TODO

Which refactoring makes more sense to do?

A:



B:

why

```
