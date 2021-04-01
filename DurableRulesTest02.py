from durable.lang import *

with ruleset('QPM'):

    @when_all((m.subject == 'Bump Height') & (m.predicate == 'Inspection') & (m.object == '3D'))
    def Height(c):
        c.assert_fact({ 'subject': c.m.subject, 'predicate': '레시피' , 'object': '설정 한다' })
        c.assert_fact({ 'subject': c.m.subject, 'predicate': '검증' , 'object': '진행 한다' })
    @when_all((m.subject == 'Bump Coplanarity') & (m.predicate == 'Inspection') & (m.object == '3D'))
    def Coplanarity(c):
        c.assert_fact({ 'subject': c.m.subject, 'predicate': '레시피' , 'object': '설정 안한다' })
        c.assert_fact({ 'subject': c.m.subject, 'predicate': '검증' , 'object': '진행 안한다' })
    @when_all((m.subject == 'Btv') & (m.predicate == 'Inspection') & (m.object == '3D'))
    def Btv(c):
        c.assert_fact({ 'subject': c.m.subject, 'predicate': '레시피' , 'object': '설정 안한다' })
        c.assert_fact({ 'subject': c.m.subject, 'predicate': '검증' , 'object': '진행 한다' })
    @when_all((m.subject == 'Bump Diameter') & (m.predicate == 'Inspection') & (m.object == '2D'))
    def Diameter(c):
        c.assert_fact({ 'subject': c.m.subject, 'predicate': '레시피' , 'object': '설정 한다' })
        c.assert_fact({ 'subject': c.m.subject, 'predicate': '검증' , 'object': '진행 한다' })
    @when_all((m.subject == 'Bridge') & (m.predicate == 'Inspection') & (m.object == '2D'))
    def Bridge(c):
        c.assert_fact({ 'subject': c.m.subject, 'predicate': '레시피' , 'object': '설정 안한다' })
        c.assert_fact({ 'subject': c.m.subject, 'predicate': '검증' , 'object': '진행 한다' })
    @when_all((m.subject == '2D Missing') & (m.predicate == 'Inspection') & (m.object == '2D'))
    def Missing(c):
        c.assert_fact({ 'subject': c.m.subject, 'predicate': '레시피' , 'object': '설정 한다' })
        c.assert_fact({ 'subject': c.m.subject, 'predicate': '검증' , 'object': '진행 안한다' })
    @when_all((m.subject == 'Barcode') & (m.predicate == 'Inspection') & (m.object == '2D'))
    def Barcode(c):
        c.assert_fact({ 'subject': c.m.subject, 'predicate': '레시피' , 'object': '설정 안한다' })
        c.assert_fact({ 'subject': c.m.subject, 'predicate': '검증' , 'object': '진행 안한다' })
    
    
    @when_all(m.predicate == 'Inspection')
    def OutputReport(c):
        c.assert_fact({ 'subject': c.m.subject, 'predicate': '셋업 레포트', 'object': '제출 한다' })
    @when_all(m.predicate == 'Align')
    def AlignMapFile(c):
        c.assert_fact({ 'subject': '모든 검사 항목은', 'predicate': c.m.predicate, 'object': '진행 한다' })
        
    @when_all(m.object == 'Both')
    def AlignMapFile(c):
        c.assert_fact({ 'subject': c.m.predicate, 'predicate': 'Map파일', 'object': '받아 온다' })
        
    @when_all(m.object == '설정 한다')
    def RecipeSet(c):
        c.assert_fact({ 'subject': c.m.subject, 'predicate': '튜닝', 'object': '필요 하다' })
       
    @when_all((m.predicate == '검증') & (m.object == '진행 한다'))
    def AcuSet(c):
        c.assert_fact({ 'subject': c.m.subject, 'predicate': '기준 Data', 'object': '필요 하다' })
        
    @when_all((m.subject == 'Bump Height') & (m.predicate == '튜닝') & (m.object == '필요 하다'))
    def Engineer(c):
        c.assert_fact({ 'subject': c.m.subject, 'predicate': '고급 엔지니어', 'object': '호출 하다' })
    @when_all((m.subject == 'Bump Diameter') & (m.predicate == '튜닝') & (m.object == '필요 하다'))
    def Illumination(c):
        c.assert_fact({ 'subject': c.m.subject, 'predicate': '조명 설정', 'object': '필요 하다' })
    
    @when_all((m.predicate == '조명 설정') & (m.object == '필요 하다'))
    def Manual(c):
        c.assert_fact({ 'subject': c.m.subject, 'predicate': '메뉴얼을', 'object': '찾아 본다' })
        
    @when_all(+m.subject)
    def Fect(c):
        print('Fact: {0} {1} {2}'.format(c.m.subject, c.m.predicate, c.m.object))
    @when_all(none(+m.subject))
    def Err(c):
        print('nothing')


assert_fact('QPM', { 'subject': 'Bump Height', 'predicate': 'Inspection', 'object': '3D' })
assert_fact('QPM', { 'subject': 'Bump Coplanarity', 'predicate': 'Inspection', 'object': '3D' })
assert_fact('QPM', { 'subject': 'Btv', 'predicate': 'Inspection', 'object': '3D' })
assert_fact('QPM', { 'subject': 'Bump Diameter', 'predicate': 'Inspection', 'object': '2D' })
assert_fact('QPM', { 'subject': '2D Missing', 'predicate': 'Inspection', 'object': '2D' })
assert_fact('QPM', { 'subject': 'Bridge', 'predicate': 'Inspection', 'object': '2D' })
assert_fact('QPM', { 'subject': 'Barcode', 'predicate': 'Inspection', 'object': '2D' })
assert_fact('QPM', { 'subject': 'Everything', 'predicate': 'Align', 'object': 'Both' })




