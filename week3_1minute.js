function getArrayMaxNumber(arr){
    // 코드 채우기
    let max = arr[0];
    for(let i = 1; i < arr.length; i++) {
        if(max < arr[i])
            max = arr[i];
        else
            continue;
    }
    return max;
}
const max = getArrayMaxNumber([10, 50, 30]);
console.log(max);