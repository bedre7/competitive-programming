
const findMedianSortedArrays = function(nums1, nums2) {
    const solution = [...nums1, ...nums2];
    solution.sort((a, b) => a - b);
    return solution.length % 2 === 0 ?
    (solution[solution.length / 2] + solution[solution.length / 2 - 1]) / 2 
    : solution[Math.floor(solution.length / 2)];
};

console.log(findMedianSortedArrays([1, 2], [3, 4]));