// 체질량 지수 계산 공식

function bmi(height, weight) {
    m_height = height / 100;
    result = weight / (m_height ** 2);
    if(result >= 26)
        return "비만";
    else if(result >= 24)
        return "과체중";
    else if(result >= 18.5)
        return "정상";
    else
        return "저체중";
}

console.log(bmi(165, 45))