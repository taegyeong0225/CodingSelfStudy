// 숫자 1~999까지 중 짝수가 몇 개인지 출력하는 코드

let count = 0;

for(let i = 1; i <= 999; i++) {
    if (i % 2 == 0) { // 짝수면
        count++;
    }
    else
        continue;
}
console.log(`짝수의 개수는 ${count}개입니다.`);