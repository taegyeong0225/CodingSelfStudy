(function(){
    const spanEl = document.querySelector("main h2 span");
    const txtArr = ['Web Publisher', 'Front-End Developer', 'Web UI Designer', 'UX Designer', 'Back-End Developer'];
    let index = 0;
    let currentTxt = txtArr[index].split("");
    function writeTxt(){
      spanEl.textContent  += currentTxt.shift(); 
      if(currentTxt.length !== 0){ 
        setTimeout(writeTxt, Math.floor(Math.random() * 100));
      }else{
        currentTxt = spanEl.textContent.split("");
        setTimeout(deleteTxt, 3000);
      }
    }
    function deleteTxt(){
      currentTxt.pop();
      spanEl.textContent = currentTxt.join("");
      if(currentTxt.length !== 0){
        setTimeout(deleteTxt, Math.floor(Math.random() * 100))
      }else{
        index = (index + 1) % txtArr.length;
        currentTxt = txtArr[index].split("");
        writeTxt();
      }
    }
    writeTxt();
  })();

 /*
  const headerEl = document.querySelector("header");
  window.addEventListener('scroll', function(){
    const browerScrollY = window.scrollY;
    if(browerScrollY > 0){
        headerEl.classList.add("active");
    } else {
        headerEl.classList.remove("active");
    }
  }); */



const headerEl = document.querySelector("header");
window.addEventListener('scroll', function(){
  requestAnimationFrame(scrollCheck);
});
function scrollCheck(){
  let browerScrollY = window.scrollY ? window.scrollY : window.pageYOffset;
  if(browerScrollY > 0){
    headerEl.classList.add("active");
  }else{
    headerEl.classList.remove("active");
  }
}
/* pageOffsetY 권장 안 함 */

/*  매뉴 이동 */
const animationMove = function(selector){
    const targetEl = document.querySelector(selector); /* 대상 노드 가져오기 */
    const browerScrollY = window.scrollY; /* 현재 Y 정보 */
    const targetScrollY = targetEl.getBoundingClientRect().top + browerScrollY;
    /* 이동 대상 위치
       getBoundingClientRect() : DOM 요소의 크기와 위치에 대한 정보를 제공하는 DOMRect 객체를 반환
       top 속성 :  targetEl 요소의 상단 경계(top)가 뷰포트 상단에서 얼마나 떨어져 있는지를 픽셀 단위로 나타내는 값 */
       window.scrollTo({ top : targetScrollY, behavior: 'smooth'});
       /* 스크롤 이동 */
};

/* 스크롤 이벤트 연결 하기 */
const scrollMoveEl = document.querySelectorAll('[data-animation-scroll="true"]');
for(let i = 0; i < scrollMoveEl.length; i++){
    scrollMoveEl[i].addEventListener('click', function(e){
        const target =  this.dataset.target;
        animationMove(target);
    });
}