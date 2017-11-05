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
test*est    {TEST}
aa|bb|cc    {DOUBLE}
while       {WHILE}
if          {IF}
not         {NOT}
or          {OR}
and         {AND}
else        {ELSE}
+           {ADD}
=           {SETV}
\+=          {A_SET}
<=          {RELOP, LE}
<           {RELOP, LT}
==          {RELOP, EQ}
!=          {RELOP, NE}
>           {RELOP, GT}
>=          {RELOP, GE}
{id}        {ID}
{number}    {NUM}

%% func


def installID():
    pass


def installNum():
    pass
