//Given an array of numbers, your function should return an array of arrays, 
//where each subarray contains all the duplicates of a particular number. 
//Subarrays should be in the same order as the first occurence of the number they contain:
//group([3, 2, 6, 2, 1, 3])
//>>> [[3, 3], [2, 2], [6], [1]]
//Assume the input is always going to be an array of numbers. 
//If the input is an empty array, an empty array should be returned.

function group(arr) {
    const result = [];

    arr.forEach(num => {
        let found = false;

        for (let i = 0; i < result.length; i++) {
            if(result[i][0] === num) {
                result[i].push(num);
                found = true;
                break;
            }
        }

        if(!found) {
            result.push([num]);
        }
    });
    return result;
}

console.log(group([3, 2, 6, 2, 1, 3]));