%% token

LT, LE, EQ, NE, GT, GE, IF, THEN, ELSE, ID, NUMBER, RELOP

%% re def

delim   (\w|\n)
ws      {delim}+
letter  (A-Z|a-z)
digit   (0-9)
id      {letter}({letter}|{digit})*
number  {digit}+(\.{digit}+)?(E(\+|-)?{digit}+)?

%% action


{ws}        {}
%%token     {TK_START}
%%syntax    {SN_START}
,           {DOT}
:           {TO}
;           {END}
'\+'        {SYN_ADD}
'\-'        {SYN_SUB}
'\/'        {SYN_DIV}
'\*'        {SYN_MUL}
'\L'        {SYN_L}
'\R'        {SYN_R}
\O          {SYN_OR}
=           {SETV}
{id}        {ID}

%% func


def installID():
    pass


def installNum():
    pass
