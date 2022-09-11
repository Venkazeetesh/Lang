#lang racket
(require(for-syntax syntax/parse))  ;Here we have imported syntax-parsing module which works as usual
(define-syntax (clauseex a)     ;Created a Macro alternative of if-else some logic
  (syntax-parse a
    ((clauseex arg:expr ...)
     #'(begin
     (define a 3) 
     (if(< a 0)         ;Instead of that here if statement is parsed.....
        0
        1))))) 