import re,marshal,dis

#dis.dis(marshal.loads(open('All-operator.pyc').read()[8:]))
print 'Rewriting Files.....!'
r = re.findall(r"LOAD_CONST.*?\((\d.*)\)",open('1.dis').read())
data1 = ('___ = ['+','.join(r[50:][:-3])+']')
data2 = marshal.loads(open('All-operator.pyc').read()[8:]).co_consts[3].co_consts[2]
data = """import base64, marshal
DIFENT_STACK = []
(lambda ___: sot.sort())(globals().update({(lambda : uc[i][p] ^ c[0][o] ** 5 != '').__code__.co_consts[3].join([ chr(i) for i in (lambda _______, _, ___: [((___ >= _______) + (___ >= ___) + (_ >= _) + ((___ > _) + (_______ <= _) + (_ <= ___)) + ((___ >= _) - (_______ > ___)) << (___ > _) + (_ <= ___) + ((_ >= _______) + (___ >= ___))) + ((___ >= _______) + (_______ != _) + (___ <= ___)), ((___ >= ___) + (___ >= ___) + (_______ != _) + ((_______ != ___) + (_______ == _______) + (___ != _______)) + (_ >= _______) * (___ >= _______) << (_______ != _) + (___ != _) + ((___ != _) + (_______ <= _______))) - (___ >= ___) * (_ != ___), ((___ > _______) + (_ >= _______) + (___ >= ___) + ((_ < ___) + (_______ < _) + (___ != _)) + (_______ >= _______) * (___ != _) << (_______ < ___) + (_______ < ___) + ((_______ != ___) + (___ != _______))) + ((_ == _) - (_______ == _) << (___ != _) + (_ < ___))])((8595258 == 8595258) + (9 != 484955) + (8595258 != 9), ((9 >= 8595258) + (484955 < 8595258) << (8595258 <= 8595258) + (9 >= 9) + (484955 != 8595258)) + ((484955 != 8595258) + (9 > 9)) << (9 > 9) + (9 <= 9), ((8595258 == 8595258) + (9 == 9) + (9 <= 8595258) + ((8595258 >= 8595258) + (9 < 8595258) + (484955 != 9)) + ((9 <= 484955) - (8595258 < 9)) << (9 <= 484955) + (8595258 <= 8595258)) - (9 != 484955) * (484955 <= 8595258)) ]): (lambda : [ {int(c.split('$')[0]) + int(c.split('$')[2]): c.split('$')[1]} for c in (lambda ___: ___.split('@'))("""+repr(data2)+""") ])()}))
(lambda : globals().update({(lambda : uc[i][p] ^ c[0][o] ** 5 != '').__code__.co_consts[3].join([ chr(i) for i in (lambda ______, __, ____: [(((____ == ____) + (______ != __) + (____ >= __) + ((____ != __) + (____ > __) + (__ < ____)) + (______ >= __) * (______ <= ____) << (__ <= ______) + (__ == __)) - (____ >= __) * (__ < ____) << (__ < ____) + (____ > ______)) - ((______ <= ______) - (__ > ____)), (((____ >= __) + (______ != ____) + (__ >= __) << (______ != __) + (______ != ____) + (____ >= ______)) + ((__ != ______) - (______ > ____)) << (______ <= ______) + (____ > __)) + ((______ >= ____) + (____ != __)), (((____ <= ____) + (__ != __) << (____ >= ______) + (______ != __) + ((____ >= ____) + (__ != ____))) - ((______ != ____) + (__ == ____)) << (__ >= __) + (____ <= ____) + (____ != ______)) + ((__ == __) + (____ <= __))])((484955 != 9) * (9 >= 9) << (8595258 >= 9) + (8595258 != 484955) + ((8595258 != 9) + (9 != 8595258)), (8595258 > 484955) + (484955 <= 8595258) + (8595258 > 9) + ((8595258 == 8595258) + (8595258 > 9) + (9 != 8595258)) + ((484955 == 484955) + (9 >= 484955)) << (9 < 484955) * (8595258 == 8595258), (9 <= 484955) + (484955 <= 8595258) + ((484955 > 9) + (8595258 <= 8595258)) + ((9 <= 484955) + (8595258 == 484955)) << (8595258 <= 8595258) + (9 != 484955)) ]): (lambda cz: cz[::-1].split('&'))((lambda x: (lambda : uc[i][p] ^ c[0][o] ** 5 != '').__code__.co_consts[3].join([ c[1][c[0]] for c in enumerate(x) ]))(sot))}))()
MAX_LENGTH = int(key[0])
"""+data1+"""
while MAX_LENGTH < int(key[2]):
    DIFENT_STACK.append(___[MAX_LENGTH])
    MAX_LENGTH += 1

exe = (lambda ____: base64.b64decode(____[1]))(key) + (lambda : uc[i][p] ^ c[0][o] ** 5 != '').__code__.co_consts[3].join([ chr(i) for i in DIFENT_STACK ])
del DIFENT_STACK
del MAX_LENGTH
del ___
del key
del sot
with open('out.pyc','wb') as f:
    f.write('03f30d0a64838e5e'.decode('hex') + exe)
"""
print 'Writting To File....!'
with open('out.py','w') as f:
	f.write(data)
	f.close()
print('Succses, Save To ``out.py``!')