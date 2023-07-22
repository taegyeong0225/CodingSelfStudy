// 100~999까지 정수 중에서 암스트롱 수에 해당하는 숫자를 모두 출력하는 코드

// 암스트롱 수 : 각 자릿수의 세제곱의 합 = 자신인 수

// 1. 각 자리의 수를 추출한다.
//  어떻게??? 첫째, 100으로 나눈 몫(parseInt() 사용)... 둘째, 첫째*100을 뺀 뒤 10으로 나눈 몫 사용... 셋째, 첫째*100 + 둘째*10을 뺀다
// 2. 세제곱을 해서 더한다.
// 3. 암스트롱 수면 출력한다.
for(let i = 100; i <= 999; i++) {
    let i_first = parseInt(i / 100);
    let i_second = parseInt((i - i_first*100) / 10);
    let i_third = i - i_first*100 - i_second * 10;
    if( i == i_first**3 + i_second**3 + i_third**3 ) 
        console.log(i);
    else
        continue;
}
