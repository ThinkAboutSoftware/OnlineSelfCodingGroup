# 객체지향의 사실과 오해 (The Essense of Object-Orientation) Discussions
## Chapter 06 객체 지도
### Discussions 01. 기능 설계 vs 구조 설계
요구사항이 변경될 가능성이 없다면 책에서 나온대로 어떻게 개발되어져도 상관없을 듯
미래의 변경될 요구사항에 유연하게 대처하기 위한 것이 소프트웨어이기 때문
하지만 미래를 대비한다? 지금도 나에게는 너무 어려운 부분..
그래서 개발자들이 기획자들과 사전미팅을 진행할 때 변경될 요구사항을 파악하기 위해
그렇게 잡아먹을 것 처럼(?)하는 것인가 생각도 들었음
요구사항에 대한 변경을 미리 차단해버리면 좋지않을까? 하는 막연한 생각도 들었지만,
생각해보면 나중에는 결국 다 변경 되었던 것 같음

### Discussions 02. 기능 설계 vs 구조 설계 현실?
기능을 중요시하는 설계가 나쁜 것은 아니라고 생각, 다만 객체지향적인 코드와 소프트웨어의 가치를
위한다면 구조 설계와 기능 설계가 적절해야한다고 생각한다. 알고 있으나 현실에 치여 그렇게 하고 있지 못하는 사람들이라면 너무 안타깝지만 사실을 알고도 외면하는 사람들은 아주 큰 잘못을 하고 있다고 생각한다. 그야말로 소프트웨어의 가치를 폄하하는 것이라고 생각하기 때문

### Discussions 03. 설계 창조 ≠ 예술
요구사항을 만족시킬 수 있는 다양한 설계안들을 저울질하면서 그 결과로 단순하면서도 유연한 설계를 창조하는 것은 공학이라기보다는 예술에 가깝다.

→ 개념을 입히고, 객체를 생성하여 객체를 움직이며 내 머릿속에 있는 세계를 반영시키는 것은 너무나 멋지고 하나의 예술처럼 느껴진다. 하지만 나도 나만의 예술작품을 만들어 보겠어! 라고 생각하는 것은 위험하지 않을까? 왜냐하면 진짜 예술은 남들과 다르고 이해하기 어려울수록 가치가 있지만
코드는 그렇지 않기때문 취향차이로 남들과 다를수는 있겠지만 난해하진 않아야됨, 그래서인지 설계의 창조는 예술이다가 아닌 예술에 가깝다~라고 한 것 같기도 함

### Discussions 04. 도메인 모델
안정적인 재료와 불안정적인 재료

→ 안정적임과 불안정적임을 나누는 기준은 요구사항의 변경 가능성인데, 책에서도 안정적인 모델은 비교적 오래 유지한다고 함 즉 [변하지 않는 것] 이라고 생각하면 안될 것 같음. 도메인 구조가 잘 잡혀 있다면 이 구조를 기반으로 작업된 기능(요구사항이 변경될 가능성이 높은 불안정적인 재료)들은 자연스럽게 대처가 가능할 수 밖에 없다는 면에서 도메인 모델이 안정적인 재료라고 하는듯?

사용자의 관점을 반영하며, 반영된 관점은 그대로 소프트웨어 개발로 이어진다.
우리가 은유를 통해 투영해야 하는 대상은 무엇인가? 그것은 바로 사용자가 도메인에 대해 생각하는 개념들이다. 즉, 소프트 웨어 객체를 창조하기 위해 우리가 은유해야 하는 대상은 바로 도메인 모델이다.
따라서 소프트웨어 객체는 그 대상이 현실적인지, 현실적이지 않은지에 상관없이 도메인 모델을 통해 표현되는 도메인 객체들을 은유해야 한다. 이것이 도메인 모델이 중요한 이유다. 도메인 모델을 기반으로 설계하고 구현하는 것은 사용자가 도메인을 바라보는 관점을 그대로 코드에 반영할 수 있게 한다. 결과적으로 표현적 차이는 줄어들 것이며, 사용자의 멘탈 모델이 그대로 코드에 녹아 스며들게 될 것이다.

→ 도메인 모델은 견고한 애플리케이션이 될 수 있도록 하는 사용자와 개발자 모두를 위한 단계

영국의 한 할머니가 로마 숫자 변역을 하기 위해 구글 검색창에 이렇게 작성하였다
”Please translate these roman numberals mcmxcviii thank you”
실례지만 이 로마자 숫자를 변역해주시겠습니까? 감사합니다. 라는 뜻인데
할머니는 화면 반대편의 구글 본사에 검색을 담당하는 직원이 있을 것이라고 생각하여
공손하게 작성했다고한다.
이렇듯 누군가가 사용할 나의 서비스는 사용자의 멘탈 모델이 반영이 될 수 밖에 없고,
모든 것이 멘탈 모델과 이어지기 때문에 소프트웨어 설계와 구현 모든 면에서 가장 중요하다고 생각
이 사례가 얼마나 멘탈 모델이 설계 구조에서 중요한지  대표적으로 보여줌

### Discussions 05. 유스케이스
5. 유스케이스
그동안의 단계들은 객체들간의 내부 설계였다면 이 단계는 고객,사용자,클라이언트와의 외부의 상호작용의 느낌 어떠한 설계 기법도 들어가지 않은 비니지니스적인 단계인 것 같다는 생각이 들었다. 

유스케이스 예제를 보고 감탄했던 부분은 책임과 협력을 만드는 과정을 교과서적인 단계 설명이 아니라 머릿속으로 상상하도록 유도시킨다는 점이다.

중도 해지 이자액 계산 유스케이스를 보며 테스트코드 작성시 만들었던 시나리오가 생각났다.
그렇다면 테스트케이스를 작성할 때 유스케이스를 기반으로 작성해도 되지 않을까?

요구사항에 대해 잘 정리된 문서가 있다면 유스케이스는 없어도 되지 않을까?
아니면 꼭 다이어그램이어야 할까? 나는 다이어그램을 보면 헷갈릴때가 많아서
오히려 표나, 글로 작성되면 더 좋을 것 같다는 생각이 들었다. 

도메인 모델 + 유스케이스(혹은 사용자 관점으로 정리된 요구사항)
객체지향적 설계에서 외부에서 바라보는 관점과, 내부에서 바라보는 관점의 이해 수준이 높을 때
좋은 코드가  나올 것 같다는 생각이듦