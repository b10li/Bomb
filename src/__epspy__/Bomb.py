## NOTE: THIS FILE IS GENERATED BY EPSCRIPT! DO NOT MODITY
from eudplib import *

def _IGVA(vList, exprListGen):
    def _():
        exprList = exprListGen()
        SetVariables(vList, exprList)
    EUDOnStart(_)

def _CGFW(exprf, retn):
    rets = [ExprProxy(None) for _ in range(retn)]
    def _():
        vals = exprf()
        for ret, val in zip(rets, vals):
            ret._value = val
    EUDOnStart(_)
    return rets

def _ARR(items):
    k = EUDArray(len(items))
    for i, item in enumerate(items):
        k[i] = item
    return k

def _SRET(v, klist):
    return List2Assignable([v[k] for k in klist])

def _SV(dL, sL):
    [d << s for d, s in zip(FlattenList(dL), FlattenList(sL))]

class _ATTW:
    def __init__(self, obj, attrName):
        self.obj = obj
        self.attrName = attrName

    def __lshift__(self, r):
        setattr(self.obj, self.attrName, r)

    def __iadd__(self, v):
        ov = getattr(self.obj, self.attrName)
        setattr(self.obj, self.attrName, ov + v)

    def __isub__(self, v):
        ov = getattr(self.obj, self.attrName)
        setattr(self.obj, self.attrName, ov - v)

    def __imul__(self, v):
        ov = getattr(self.obj, self.attrName)
        setattr(self.obj, self.attrName, ov * v)

    def __idiv__(self, v):
        ov = getattr(self.obj, self.attrName)
        setattr(self.obj, self.attrName, ov / v)

    def __iand__(self, v):
        ov = getattr(self.obj, self.attrName)
        setattr(self.obj, self.attrName, ov & v)

    def __ior__(self, v):
        ov = getattr(self.obj, self.attrName)
        setattr(self.obj, self.attrName, ov | v)

    def __ixor__(self, v):
        ov = getattr(self.obj, self.attrName)
        setattr(self.obj, self.attrName, ov ^ v)

class _ARRW:
    def __init__(self, obj, index):
        self.obj = obj
        self.index = index

    def __lshift__(self, r):
        self.obj[self.index] = r

    def __iadd__(self, v):
        ov = self.obj[self.index]
        self.obj[self.index] = ov + v

    def __isub__(self, v):
        ov = self.obj[self.index]
        self.obj[self.index] = ov - v

    def __imul__(self, v):
        ov = self.obj[self.index]
        self.obj[self.index] = ov * v

    def __idiv__(self, v):
        ov = self.obj[self.index]
        self.obj[self.index] = ov / v

    def __iand__(self, v):
        ov = self.obj[self.index]
        self.obj[self.index] = ov & v

    def __ior__(self, v):
        ov = self.obj[self.index]
        self.obj[self.index] = ov | v

    def __ixor__(self, v):
        ov = self.obj[self.index]
        self.obj[self.index] = ov ^ v

def _L2V(l):
    ret = EUDVariable()
    if EUDIf()(l):
        ret << 1
    if EUDElse()():
        ret << 0
    EUDEndIf()
    return ret

def _MVAR(vs):
    return List2Assignable([
        v.makeL() if IsEUDVariable(v) else EUDVariable() << v
        for v in FlattenList(vs)])

def _LSH(l, r):
    if IsEUDVariable(l):  return f_bitlshift(l, r)
    else: return l << r

## NOTE: THIS FILE IS GENERATED BY EPSCRIPT! DO NOT MODITY

# (Line 1) import Map;
import Map
# (Line 2) import Player;
import Player
# (Line 3) import Helpers;
import Helpers
# (Line 5) const BombQ						= EUDArray(20);
BombQ = _CGFW(lambda: [EUDArray(20)], 1)[0]
# (Line 6) var QIndex, QCount, boom;
QIndex, QCount, boom = EUDCreateVariables(3)
# (Line 8) const row						= Map.row;
row = _CGFW(lambda: [Map.row], 1)[0]
# (Line 9) const col						= Map.col;
col = _CGFW(lambda: [Map.col], 1)[0]
# (Line 11) const Computer					= Helpers.Computer;
Computer = _CGFW(lambda: [Helpers.Computer], 1)[0]
# (Line 12) const UnitID_Player 			= Helpers.UnitID_Player;
UnitID_Player = _CGFW(lambda: [Helpers.UnitID_Player], 1)[0]
# (Line 13) const UnitID_Bomb				= Helpers.UnitID_Bomb;
UnitID_Bomb = _CGFW(lambda: [Helpers.UnitID_Bomb], 1)[0]
# (Line 14) const UnitID_Fire				= Helpers.UnitID_Fire;
UnitID_Fire = _CGFW(lambda: [Helpers.UnitID_Fire], 1)[0]
# (Line 15) const UnitID_Wall				= Helpers.UnitID_Wall;
UnitID_Wall = _CGFW(lambda: [Helpers.UnitID_Wall], 1)[0]
# (Line 16) const UnitID_Box				= Helpers.UnitID_Box;
UnitID_Box = _CGFW(lambda: [Helpers.UnitID_Box], 1)[0]
# (Line 18) const loc2 = $L('loc2');
loc2 = _CGFW(lambda: [GetLocationIndex('loc2')], 1)[0]
# (Line 19) const loc3 = $L('loc3');
loc3 = _CGFW(lambda: [GetLocationIndex('loc3')], 1)[0]
# (Line 20) const scale						= Helpers.scale;
scale = _CGFW(lambda: [Helpers.scale], 1)[0]
# (Line 24) function NewBomb(unitEpd)
# (Line 25) {
@EUDFunc
def NewBomb(unitEpd):
    # (Line 26) const x, y = Map.GetTileIndex(unitEpd);
    x, y = List2Assignable([Map.GetTileIndex(unitEpd)])
    # (Line 27) Map.SetMapXY(x, y, unitEpd);
    Map.SetMapXY(x, y, unitEpd)
    # (Line 28) }
    # (Line 30) function Push(unitEpd)

# (Line 31) {
@EUDFunc
def Push(unitEpd):
    # (Line 32) BombQ[QIndex] = unitEpd;
    _ARRW(BombQ, QIndex) << (unitEpd)
    # (Line 33) QIndex = QIndex + 1; //Index ++
    QIndex << (QIndex + 1)
    # (Line 34) QCount = QCount + 1; //Count ++
    QCount << (QCount + 1)
    # (Line 35) }
    # (Line 36) function InitQ()

# (Line 37) {
@EUDFunc
def InitQ():
    # (Line 38) for(var i=0; i<20; i++)
    i = EUDVariable()
    i << (0)
    if EUDWhile()(i >= 20, neg=True):
        def _t2():
            i.__iadd__(1)
        # (Line 39) BombQ[i] = 0;
        _ARRW(BombQ, i) << (0)
        # (Line 40) QIndex = 0;
        EUDSetContinuePoint()
        _t2()
    EUDEndWhile()
    QIndex << (0)
    # (Line 41) QCount = 0;
    QCount << (0)
    # (Line 42) }
    # (Line 44) function CreateItem(location);

# (Line 45) function Explosion(unitEpd);
# (Line 46) function CreateFire(fireRange, direction, _x, _y);
# (Line 47) function Boom();
# (Line 48) function CheckBomb()
# (Line 49) {// 폭탄 타이머 체크, 폭발 시작
@EUDFunc
def CheckBomb():
    # (Line 50) for(var i=0; i<row; i++)
    i = EUDVariable()
    i << (0)
    if EUDWhile()(i >= row, neg=True):
        def _t2():
            i.__iadd__(1)
        # (Line 51) {
        # (Line 52) for(var j=0; j<col; j++)
        j = EUDVariable()
        j << (0)
        if EUDWhile()(j >= col, neg=True):
            def _t4():
                j.__iadd__(1)
            # (Line 53) {
            # (Line 54) const unitEpd = Map.GetMapXY(i, j);
            unitEpd = Map.GetMapXY(i, j)
            # (Line 55) if( unitEpd != 0 ||
            _t5 = EUDIf()
            # (Line 56) unitEpd != UnitID_Fire ||
            # (Line 57) unitEpd != UnitID_Box ||
            # (Line 58) unitEpd != UnitID_Wall)
            if _t5(EUDSCOr()(unitEpd == 0, neg=True)(unitEpd == UnitID_Fire, neg=True)(unitEpd == UnitID_Box, neg=True)(unitEpd == UnitID_Wall, neg=True)()):
                # (Line 59) {
                # (Line 60) if(MemoryEPD(unitEpd + 0x114/4, Exactly, 1))
                if EUDIf()(MemoryEPD(unitEpd + 0x114 // 4, Exactly, 1)):
                    # (Line 61) {
                    # (Line 62) Push(unitEpd);
                    Push(unitEpd)
                    # (Line 63) }
                    # (Line 64) }
                EUDEndIf()
                # (Line 65) }
            EUDEndIf()
            # (Line 66) }
            EUDSetContinuePoint()
            _t4()
        EUDEndWhile()
        # (Line 67) var k = 0;
        EUDSetContinuePoint()
        _t2()
    EUDEndWhile()
    k = EUDVariable()
    k << (0)
    # (Line 68) while(QCount > 0) //Count > 0
    if EUDWhile()(QCount <= 0, neg=True):
        # (Line 69) {
        # (Line 70) Explosion(BombQ[k]);
        Explosion(BombQ[k])
        # (Line 71) k++;
        k.__iadd__(1)
        # (Line 72) QCount = QCount - 1; // Count--
        QCount << (QCount - 1)
        # (Line 73) }
        # (Line 74) if(QIndex > 0)
    EUDEndWhile()
    if EUDIf()(QIndex <= 0, neg=True):
        # (Line 75) {
        # (Line 76) Boom();
        Boom()
        # (Line 77) InitQ();
        InitQ()
        # (Line 78) }
        # (Line 79) }
    EUDEndIf()
    # (Line 81) function Boom()

# (Line 82) {// 체크한 블록을 처리함. 실질적인 폭발
@EUDFunc
def Boom():
    # (Line 83) boom = 1;
    boom << (1)
    # (Line 84) for(var i=0; i<row; i++)
    i = EUDVariable()
    i << (0)
    if EUDWhile()(i >= row, neg=True):
        def _t2():
            i.__iadd__(1)
        # (Line 85) {
        # (Line 86) for(var j=0; j<col; j++)
        j = EUDVariable()
        j << (0)
        if EUDWhile()(j >= col, neg=True):
            def _t4():
                j.__iadd__(1)
            # (Line 87) {
            # (Line 88) if(Map.GetMapXY(i, j) == UnitID_Fire)
            if EUDIf()(Map.GetMapXY(i, j) == UnitID_Fire):
                # (Line 89) {
                # (Line 90) Map.SetMapXY(i, j, 0);
                Map.SetMapXY(i, j, 0)
                # (Line 91) const x, y = Map.GetTileXY(i, j);
                x, y = List2Assignable([Map.GetTileXY(i, j)])
                # (Line 92) Helpers.EUDSetLocation(loc2, x, y);
                Helpers.EUDSetLocation(loc2, x, y)
                # (Line 93) KillUnitAt(All, '(men)', loc2+1, $Force1);
                DoActions(KillUnitAt(All, '(men)', loc2 + 1, 18))
                # (Line 94) RemoveUnitAt(All, '(any unit)', loc2+1, Computer);
                DoActions(RemoveUnitAt(All, '(any unit)', loc2 + 1, Computer))
                # (Line 95) CreateUnit(1, UnitID_Fire, loc2+1, Computer);
                DoActions(CreateUnit(1, UnitID_Fire, loc2 + 1, Computer))
                # (Line 96) }
                # (Line 97) if(Map.GetMapXY(i, j) == Helpers.DeadBox)
            EUDEndIf()
            if EUDIf()(Map.GetMapXY(i, j) == Helpers.DeadBox):
                # (Line 98) {
                # (Line 99) Map.SetMapXY(i, j, 0);
                Map.SetMapXY(i, j, 0)
                # (Line 100) const x, y = Map.GetTileXY(i, j);
                x, y = List2Assignable([Map.GetTileXY(i, j)])
                # (Line 101) Helpers.EUDSetLocation(loc2, x, y);
                Helpers.EUDSetLocation(loc2, x, y)
                # (Line 102) RemoveUnitAt(All, '(men)', loc2+1, Computer);
                DoActions(RemoveUnitAt(All, '(men)', loc2 + 1, Computer))
                # (Line 103) CreateItem(loc2);
                CreateItem(loc2)
                # (Line 104) }
                # (Line 105) }
            EUDEndIf()
            # (Line 106) }
            EUDSetContinuePoint()
            _t4()
        EUDEndWhile()
        # (Line 107) KillUnit(UnitID_Fire, Computer);
        EUDSetContinuePoint()
        _t2()
    EUDEndWhile()
    DoActions(KillUnit(UnitID_Fire, Computer))
    # (Line 108) boom = 0;
    boom << (0)
    # (Line 109) }
    # (Line 111) function Explosion(unitEpd)

# (Line 112) {// 폭탄 사거리에 맞게 불 생성
@EUDFunc
def Explosion(unitEpd):
    # (Line 113) const player = dwbreak(dwread_epd(unitEpd + 0x4C / 4))[[2]];
    player = f_dwbreak(f_dwread_epd(unitEpd + 0x4C // 4))[2]
    # (Line 114) const fireRange = Player.GetBombRange(player);
    fireRange = Player.GetBombRange(player)
    # (Line 116) const x, y = Map.GetTileIndex(unitEpd); // 해당좌표의 unitEpd
    x, y = List2Assignable([Map.GetTileIndex(unitEpd)])
    # (Line 117) Map.SetMapXY(x, y, 0);  // 초기화
    Map.SetMapXY(x, y, 0)
    # (Line 119) const x2, y2 = Map.GetTileXY(x, y);
    x2, y2 = List2Assignable([Map.GetTileXY(x, y)])
    # (Line 120) Helpers.EUDSetLocation(loc2, x2, y2);
    Helpers.EUDSetLocation(loc2, x2, y2)
    # (Line 121) RemoveUnitAt(1, UnitID_Bomb, loc2+1, player);
    DoActions(RemoveUnitAt(1, UnitID_Bomb, loc2 + 1, player))
    # (Line 123) for(var i=0; i<4; i++)
    i = EUDVariable()
    i << (0)
    if EUDWhile()(i >= 4, neg=True):
        def _t2():
            i.__iadd__(1)
        # (Line 124) {
        # (Line 125) CreateFire(fireRange, i, x, y);
        CreateFire(fireRange, i, x, y)
        # (Line 126) }
        # (Line 127) }
        EUDSetContinuePoint()
        _t2()
    EUDEndWhile()
    # (Line 131) function CreateFire(fireRange, direction, _x, _y)

# (Line 132) {// 불생성 지역에, 있는 지형/폭탄 탐지
@EUDFunc
def CreateFire(fireRange, direction, _x, _y):
    # (Line 133) Map.SetMapXY(_x, _y, UnitID_Fire);
    Map.SetMapXY(_x, _y, UnitID_Fire)
    # (Line 134) for(var j=1; j<=fireRange; j++)
    j = EUDVariable()
    j << (1)
    if EUDWhile()(j <= fireRange):
        def _t2():
            j.__iadd__(1)
        # (Line 135) {
        # (Line 136) var x = _x;
        x = EUDVariable()
        x << (_x)
        # (Line 137) var y = _y;
        y = EUDVariable()
        y << (_y)
        # (Line 139) if(direction == 0)
        if EUDIf()(direction == 0):
            # (Line 140) {
            # (Line 141) if(x < j) x = 0;
            if EUDIf()(x >= j, neg=True):
                x << (0)
                # (Line 142) else x = x - j;
            if EUDElse()():
                x << (x - j)
                # (Line 143) }
            EUDEndIf()
            # (Line 144) if(direction == 1)
        EUDEndIf()
        if EUDIf()(direction == 1):
            # (Line 145) {
            # (Line 146) if(y < j) y = 0;
            if EUDIf()(y >= j, neg=True):
                y << (0)
                # (Line 147) else y = y - j;
            if EUDElse()():
                y << (y - j)
                # (Line 148) }
            EUDEndIf()
            # (Line 149) if(direction == 2)
        EUDEndIf()
        if EUDIf()(direction == 2):
            # (Line 150) {
            # (Line 151) if(x + j > row) x = row;
            if EUDIf()(x + j <= row, neg=True):
                x << (row)
                # (Line 152) else x = x + j;
            if EUDElse()():
                x << (x + j)
                # (Line 153) }
            EUDEndIf()
            # (Line 154) if(direction == 3)
        EUDEndIf()
        if EUDIf()(direction == 3):
            # (Line 155) {
            # (Line 156) if(y + j > col) y = col;
            if EUDIf()(y + j <= col, neg=True):
                y << (col)
                # (Line 157) else y = y + j;
            if EUDElse()():
                y << (y + j)
                # (Line 158) }
            EUDEndIf()
            # (Line 160) if (Map.GetMapXY(x, y) == UnitID_Wall) return;	// Imapssible
        EUDEndIf()
        if EUDIf()(Map.GetMapXY(x, y) == UnitID_Wall):
            EUDReturn()
            # (Line 161) else if (Map.GetMapXY(x, y) == UnitID_Fire) 	// Fire
        if EUDElseIf()(Map.GetMapXY(x, y) == UnitID_Fire):
            # (Line 162) Map.SetMapXY(x, y, UnitID_Fire);
            Map.SetMapXY(x, y, UnitID_Fire)
            # (Line 163) else if (Map.GetMapXY(x, y) == 0) 				// Empty
        if EUDElseIf()(Map.GetMapXY(x, y) == 0):
            # (Line 164) Map.SetMapXY(x, y, UnitID_Fire);
            Map.SetMapXY(x, y, UnitID_Fire)
            # (Line 165) else if (Map.GetMapXY(x, y) == UnitID_Box) 		// Breakable
        if EUDElseIf()(Map.GetMapXY(x, y) == UnitID_Box):
            # (Line 166) {
            # (Line 167) Map.SetMapXY(x, y, Helpers.DeadBox);
            Map.SetMapXY(x, y, Helpers.DeadBox)
            # (Line 168) return;
            EUDReturn()
            # (Line 169) }
            # (Line 170) else if (Map.GetMapXY(x, y) == Helpers.DeadBox) return;
        if EUDElseIf()(Map.GetMapXY(x, y) == Helpers.DeadBox):
            EUDReturn()
            # (Line 171) else 											// bomb (unitEpd)
            # (Line 172) {
        if EUDElse()():
            # (Line 173) const unitEpd = Map.GetMapXY(x, y);
            unitEpd = Map.GetMapXY(x, y)
            # (Line 174) Push(unitEpd);
            Push(unitEpd)
            # (Line 175) }
            # (Line 176) }
        EUDEndIf()
        # (Line 177) }
        EUDSetContinuePoint()
        _t2()
    EUDEndWhile()
    # (Line 179) function CreateItem(location)

# (Line 180) {
@EUDFunc
def CreateItem(location):
    # (Line 181) if(Helpers.GetRandom(0,2))// 0~1
    if EUDIf()(Helpers.GetRandom(0, 2)):
        # (Line 182) {
        # (Line 183) const randNum = Helpers.GetRandom(0, 9)%6; //0~8 -> 0~5
        randNum = Helpers.GetRandom(0, 9) % 6
        # (Line 184) CreateUnit(1, Helpers.ItemList[randNum], location +1, Computer);
        DoActions(CreateUnit(1, Helpers.ItemList[randNum], location + 1, Computer))
        # (Line 185) }
        # (Line 186) }
    EUDEndIf()
