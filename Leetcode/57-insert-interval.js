/**
 * @param {number[][]} intervals
 * @param {number[]} newInterval
 * @return {number[][]}
 */
 var insert = function(intervals, newInterval) {
    intervals.push(newInterval);
    intervals = intervals.sort((a, b) => a[0] - b[0]);
    
    merged = []
    
    for (const [start, end] of intervals){
        if (merged.length != 0 && merged.at(-1)[1] >= start)
            merged.at(-1)[1] = Math.max(end, merged.at(-1)[1]);
        else
            merged.push([start, end]);
    }
    
    return merged;
};