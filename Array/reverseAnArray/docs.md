# Problem Statement.

To reverse the elements of an Array.

let arr[n] be an array of n elements.
Then to arrange array, a[0] be replaced with a[n-1],
and a[1] be replaced with a[n-2].

# Solutions

## 1. Empty Array
 We can introduce an empty array which will be
 filled with the elements of arr[n] but in reverse order.

### Things I learned

- for loops increment index by default meaning, there is
no need for specifying index.

- newArr = []  # initialized but not declared.
When an array is not declared index assignments fails.
use python's append() function for such cases.

