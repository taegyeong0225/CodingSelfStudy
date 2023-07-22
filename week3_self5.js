// 매개변수를 배열로 전달받아 배열의 요소 중 가장 큰 수를 찾아 반환

function findMax(arr) {
    let max = arr[0];
    for(let i = 1; i < arr.length; i++) {
        if(max < arr[i])
            max = arr[i];
        else
            continue;
    }
    return max
}

console.log(findMax([34, 56, 12, 6, 23, 8]))