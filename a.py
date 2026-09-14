#파이썬은 패키지로 분할된 개별적인 모듈로 구성
#상대경로 : ..(부모 디렉토리). (현재 디렉토리);

#1)import 패키지명, 하위패키지.모듈명;
import pro_test.test1.module1
import pro_test.test2.module2

pro_test.test1.module1.mod1_test()
pro_test.test1.module1.mod2_test()

pro_test.test2.module2.mod3_test()
pro_test.test2.module2.mod4_test()


#)from 패키지명 하위패키지 import 모듈명
from pro_test.test1 import module1
from pro_test.test2 import module2

module1.mod1_test()
module1.mod2_test()

module2.mod3_test()
module2.mod4_test()

#215.p
#from 패키지명 import * *전부다 
from pro_test.test1 import *
from pro_test.test2 import *

module1.mod1_test()
module1.mod2_test()

module2.mod3_test()
module2.mod4_test()

#231.p 예외처리

