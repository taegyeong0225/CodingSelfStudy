// 2. 다음 배열의 요소 중 가장 큰 수를 출력하는 코드를 완성하세요
const arr = [10, 120, 30, 50, 20];

(function maxNum(arr){
    max = arr[0];
    for(let i = 0; i < arr.length; i++) {
        if(arr[i] > max)
            max = arr[i];
        else
            continue;
    }
    console.log(max);
})(arr);

// 교재 답안
// const arr = [10, 120, 30, 50, 20];
// arr.sort(function(a, b){
//        if(a < b) return 1;
//        else if(a > b) return -1;
//        else return 0;
// })
// console.log(arr[0]) 