## Project Summary

The Goal of my project was to improve the implementation of the Asynchronous Input outpout (AIO) interface in RTEMS. Prior to my contribution the implementation laked some functionalitieds and some methods did not adhere fully to the posix specifications. The plan for the project was divided in two parts, in the first half of the coding period my focus wouldf be centered around fixing the issue i found in the ewxisiting aio methods and by addressing the missing functionalities. In the second half the goal was to implement the two missing methods, particularly lio_listio() and aio_ssupend().

## My Contributions

Below, you'll find a table containing a summary of the various contribution i made and the planned ones, with their status and the related Merge requests. After the table there will be a short desctiption outlining the scope of each contribution. For each completed contribution there will be a blog post descibing my work with more detail.

| Contribution                                                        | Status    | Related MR             | Blog Posts |
| :------------------------------------------------------------------ | :-------: | :--------------------- | :--------: |
| Review and merge existing patches                                   | Completed | !40 !41 !42            |  |
| Correct the behavior of aio_return() and aio_error()                | Completed | !85                    |  |
| Add support for O_DSYNC in aio_fsync()                              | Completed | !128                   |  |
| Add notification at request completion                              | Completed | !118                   |  |
| Implement lio_listio()                                              | WIP       | !188 ( Draft )         | - |
| Update documentation                                                | Completed | !56 !26                |  |

####Review and merge existing patches
description
####Correct the behavior of aio_return() and aio_error()
description
####Add support for O_DSYNC in aio_fsync()
description
####Add notification at request completion
description
####Implement lio_listio()
description
####Update documentation
description
## What I learned
text
