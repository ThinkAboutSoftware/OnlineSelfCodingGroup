# Object discussions



## 들어가며


### Discussion 1 - 프롤로그(PROLOG)

프롤로그(PROLOG) - 논리형 패러다임을 수용한 대표적인 언어

논리형 언어라는 단어가 갑자기 생소하게 느껴짐 - 수학적?

그리고 논리형 언어면 컴퓨터가 제일 좋아하는 거 아닐까 하지만 그걸로는 부족하니 객체지향적 언어가 나온거겠지 라는 생각도 들었다.

그리고 프롤로그라고 해서 책의 첫 인사 그 뜻인건가 싶었지만 그건 Prologue였다 ㅎㅎ; 


### Discussion 2 - 프로그래밍 패러다임의 수용성

두 패러다임이 함께 존재할 수 있다.

프로그래밍 패러다임은 혁명적(revolutionary)이 아니라 발전적(evolutionary)이다.

무조건적으로 모든 상황에서 객체지향이 최고다가 아니라 필요할 때 쓰는게 중요하구나 싶은 생각이 든다.

그런데 필요한지 아닌지 판단기준은 어떻게 정하는 걸까 



## 01 객체, 설계


### Discussion 3 - 이론이 먼저일까, 실무가 먼저일까? 

로버트 L.글래스(Robert L. Glass) - 이론보다 실무가 먼저다. 

분석이나 설계가 이론이라고 생각을 했었는데 그 이유가 바보같고 어이없지만 코딩을 제외한 문서작성은 이론적인거라고 생각했던거 같다.

하루라도 빨리 객체지향적 프로그래밍을 해보고 싶은 열망?갈망이 생겼다. 조급한 마음도 든다.


### Discussion 4 - 의존성의 밸런스는 어떻게 맞춰나가야 하지? 

결합도는 낮춰야 하지만 그렇다고 객체사이에는 없어서는 안되는 의존성 역시나 밸런스조절이 진짜 힘들거 같다.


### Discussion 5 - 비록 현실에서는 수동적인 존재라고 하더라도 일단 객체지향의 세계에 들어오면 모든 것이 능동적이고 자율적인 존재로 바뀐다. -의인화

레베카 워프스브록님의 객체를 의인화한다는 표현에서 객체에 대한 애정이 느껴진다고 하면 내가 오버하는 것일까

객체가 생명과 지능을 가진 싱싱한 존재로 다시 태어난다니 나도 체감할 수 있는 날이 오겠지?



## 03 객체, 설계


### Discussion 6 - 어떤 객체도 섬이 아니다[켄트 벡]

객체 세계에는 왕따는 없겠다는 생각이 들어서 이상적으로 느껴진다.


### Discussion 7 - 객체가 메시지를 선택하는 것이 아니라 메시지가 객체를 선택한다[Metz12]

이상하다 객체는 자유롭다고 했는데 메시지를 선택할 수 없다라는건  무슨 의미지라는 생각이 들었다.
그러나 메시지가 객체를 선택해야 하는 이유를 보니 아무리 자유롭다고 해도 최소한의 규칙이 있는거 아닐까라는 생각이 들었다.
 

### Discussion 8 - 객체지향 패러다임에 갓 입문한 사람들이 가장 쉽게 빠지는 실수는 객체의 행동이 아니라 상태에 초점을 맞추는 것이다.

아직 객체지향 프로그래밍을 해본 경험은 없지만 나도 이러할 거 같다라는 생각이 든다. 
그건 상태관리를 하는 리액트가 생각나서 그런거 같기도 하다.


### Discussion 9- 역할은 객체가 참여할 수 있는 일종의 슬롯이다.

개인적으로는 역할이 되게 매력적으로 느껴졌다. 객체가 자유롭다는걸 제대로 와닿게 하는 핵심중 하나라고 할까. 


### Discussion 10 - 연극 안에서 배역을 연기하는 배우라는 은유는 협력 안에서 역할을 수행하는 객체라는 관점이 가진 입체적인 측면들을 훌륭하게 담아낸다. 이 부분을 읽고 막연했던 객체에 대해 조금은 이해하게 된거 같다. & 역할은 객체의 페르소나다.

이 부분을 보고 든 생각이 나라는 사람이  상대방의 기준에 따라서 롤이 바뀌는 게 객체가 배역을 연기하는 배우가 되는거와 맥락상 같은게 아닐까 라는 생각이 들었다.

가족들을 예시로 든다면  엄마의 관점에서는 딸일테고 동생들이 보기에는 언니나 누나가 될테고 역할에 맞는 액션을 취하게 되는게 객체와 비슷한게 아닌가라는 생각이 든다.


### Discussion 11 - 협력은 연극과 동일하고 코드는 극본과 동일하다.

왠지 낭만적이다 이렇게 비유할 수 있다니! 그러면 개발자는 시나리오 작가인것인가?



## 04 설계 품질과 트레이드 오프

### Discussion 12

이번 장에서는 데이터 중심의 설계로 코드를 작성하며 나쁜 설계의 예시를 보여준다.
그러고 언어는 다르지만 나또한 이런식으로 코드를 짜고 있었다는 생각에 뜨끔해진다.

### Discussion 13 - 좋은 설계란 오늘의 기능을 수행하면서 내일의 변경을 수용할 수 있는 설계다.

좋은 설계하면 지금 나에게 떠오르는건 멘토님이 예전에 냥터레스트 서버부분을 리팩토링해주신 코드다.

그당시 객체지향 코드란 이런거구나 라고 감탄은 하였지만 어려워서 감히 merge도 못했는데 지금 다시 보니 

데이터 중심의 내코드가 이렇게 쪼개져서 협력을 하고 있구나 라는 생각이 먼저 들었다.

기존의 내코드는 하나가 변경되면 결합도가 높아서 전체코드를 수정했었는데 멘토님 코드라면 필요한 부분만 수정하면

다른 객체들의 코드를 수정할 일은 없으니 낮은 결합도를 가진거구나라는 생각이 들었다.

또 유지보수를 위한 코드를 만들어야 한다는게 이런 의미구나라는 생각도 들었다.


### Discussion 14 - "인터페이스에 대해 프로그래밍하라[GOF94]"

멘토님의 코드를 보면 구현되는 부분은 각각 나누어져 내부에 있으며  다른 객체들과 협력할때는 가지고온 const가 인터페이스역할을 하는거 같다
이게 내가 맞게 생각하는걸까? 

### Discussion 15 - private으로 설정해도 접근자와 수정자를 통해 속성을 외부로 제공하고 있다면 위반하는 것이다?

private안에 있으면 무조건 캡슐화가 되는거라고 생각했는데 그게 아니라는게 



### Discussion 16 - 데이터 중심 설계는 객체를 고립시킨채 오퍼레이션을 정의하도록 만든다

내코드는 당연하게도 고립되어 있었겠다 싶어져서 갑자기 코드에게 미안(?)해진다. 앞으로는 객체지향적인 생각을 하도록 의도적으로라도 노력을 해야겠다는 생각이 든다.







