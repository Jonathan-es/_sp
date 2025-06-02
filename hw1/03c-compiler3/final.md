# 期末作業
# 資工二 111210554 陳家盛

## 習題一

[HW1](https://github.com/Jonathan-es/_sp/tree/main/hw1/03c-compiler3)

參考同學，使用ChatGPT調試問題
```
// DOWHILE = do STMT while (E);
void DOWHILE() {
  int doBegin = nextLabel();
  int doEnd = nextLabel();
  emit("(L%d)\n", doBegin);
  skip("do");
  STMT();
  skip("while");
  skip("(");
  int e = E();
  skip(")");
  skip(";");
  emit("if t%d goto L%d\n", e, doBegin);
  emit("(L%d)\n", doEnd);
}

```

---

## 習題二

[hw2](https://github.com/Jonathan-es/_sp/tree/main/hw2)
[result](https://github.com/Jonathan-es/_sp/blob/main/hw2/result.md)

參考同學，使用ChatGPT調試問題
```
$ ./test.sh
# 以下省略...

$ ./c4 -s test/power2.c
1: #include <stdio.h>
2: int power2(int n) {
3:    int r, i;
4:    r = 1;
    ENT  2
    LLA  -1
    PSH 
    IMM  1
    SI  
5:    i = 1;
    LLA  -2
    PSH 
    IMM  1
    SI  
6:    while (i<=n) {
    LLA  -2
    LI  
    PSH 
    LLA  2
    LI  
    LE  
    BZ   0
7:       r = r*2;
    LLA  -1
    PSH 
    LLA  -1
    LI  
    PSH 
    IMM  2
    MUL 
    SI  
8:       i++;
    LLA  -2
    PSH 
    LI  
    PSH 
    IMM  1
    ADD 
    SI  
    PSH 
    IMM  1
    SUB 
9:    }
10:    return r;
    JMP  939819128
    LLA  -1
    LI  
    LEV 
11: }
    LEV 
12: 
13: int main() {
14:    printf("power2(3)=%d\n", power2(3));
    ENT  0
    IMM  940081152
    PSH 
    IMM  3
    PSH 
    JSR  939819016
    ADJ  1
    PSH 
    PRTF
    ADJ  2
```

---

## 習題三

[hw3](https://github.com/Jonathan-es/_sp/tree/main/hw3)

參考同學，使用ChatGPT調試問題
```
```
```
while (tk = *p) {
    ++p;
    if (tk == '\n') { // 換行
      if (src) {
        printf("%d: %.*s", line, p - lp, lp); // 印出該行
        lp = p; // lp = p = 新一行的原始碼開頭
        while (le < e) { // 印出上一行的所有目的碼
          printf("  %d: %8.4s", le+1, &"LLA ,IMM ,JMP ,JSR ,BZ  ,BNZ ,ENT ,ADJ ,LEV ,LI  ,LC  ,SI  ,SC  ,PSH ,"
                           "OR  ,XOR ,AND ,EQ  ,NE  ,LT  ,GT  ,LE  ,GE  ,SHL ,SHR ,ADD ,SUB ,MUL ,DIV ,MOD ,"
                           "OPEN,READ,CLOS,PRTF,MALC,FREE,MSET,MCMP,EXIT,"[*++le * 5]);
          if (*le <= ADJ) printf("%d\n", *++le); else printf("\n"); // LLA ,IMM ,JMP ,JSR ,BZ  ,BNZ ,ENT ,ADJ 有一個參數。
        }
      }
      ++line;
    }
  }
```

---

## 習題四

[hw3](https://github.com/Jonathan-es/_sp/tree/main/hw4)

參考同學，使用ChatGPT調試問題
```
# -----------------------------------------------------------------------------
# A 64-bit function that returns the multiple value of its three 64-bit integer
# arguments.  The function has signature:
#
#   int64_t mul3(int64_t x, int64_t y, int64_t z)
#
# Note that the parameters have already been passed in rdi, rsi, and rdx.  We
# just have to return the value in rax.
# -----------------------------------------------------------------------------

        .globl  mul3
        
        .text
mul3:
        mov     %rdi, %rax
        imulq     %rsi, %rax
        imulq   %rdx, %rax
        ret    
```

---

## 習題五

[hw5](https://github.com/Jonathan-es/_sp/tree/main/hw5)

參考同學，使用ChatGPT調試問題

```
```
```
	.file	"power.c"
	.text
	.globl	_power
	.def	_power;	.scl	2;	.type	32;	.endef
_power:
LFB10:
	.cfi_startproc
	pushl	%ebp
	.cfi_def_cfa_offset 8
	.cfi_offset 5, -8
	movl	%esp, %ebp
	.cfi_def_cfa_register 5
	subl	$16, %esp
	movl	$1, -4(%ebp)
	movl	$0, -8(%ebp)
	jmp	L2
L3:
	movl	-4(%ebp), %eax
	imull	8(%ebp), %eax
	movl	%eax, -4(%ebp)
	addl	$1, -8(%ebp)
L2:
	movl	-8(%ebp), %eax
	cmpl	12(%ebp), %eax
	jl	L3
	movl	-4(%ebp), %eax
	leave
	.cfi_restore 5
	.cfi_def_cfa 4, 4
	ret
	.cfi_endproc
LFE10:
	.def	___main;	.scl	2;	.type	32;	.endef
	.section .rdata,"dr"
LC0:
	.ascii "result = %d\12\0"
	.text
	.globl	_main
	.def	_main;	.scl	2;	.type	32;	.endef
_main:
LFB11:
	.cfi_startproc
	pushl	%ebp
	.cfi_def_cfa_offset 8
	.cfi_offset 5, -8
	movl	%esp, %ebp
	.cfi_def_cfa_register 5
	andl	$-16, %esp
	subl	$16, %esp
	call	___main
	movl	$3, 4(%esp)
	movl	$2, (%esp)
	call	_power
	movl	%eax, 4(%esp)
	movl	$LC0, (%esp)
	call	_printf
	movl	$0, %eax
	leave
	.cfi_restore 5
	.cfi_def_cfa 4, 4
	ret
	.cfi_endproc
LFE11:
	.ident	"GCC: (MinGW.org GCC-6.3.0-1) 6.3.0"
	.def	_printf;	.scl	2;	.type	32;	.endef
```

```
