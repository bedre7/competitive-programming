var merge = function(intervals) {
    if (intervals.length == 0) return intervals;
    
    intervals.sort((a, b) => a[0] - b[0]);
    let merged = [];
    
    for ([start, end] of intervals)
    {
        if(merged.length !=0 && merged.at(-1)[1] >= start)
            merged.at(-1)[1] = Math.max(merged.at(-1)[1], end);
        else merged.push([start, end]);
    }
    
    return merged;
};