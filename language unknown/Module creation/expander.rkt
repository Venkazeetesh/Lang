#lang racket/base

(provide
  (except-out (all-from-out racket/base) #%module-begin) ;;Here provide declares all the function which taken from module
  (rename-out [module-begin #%module-begin]) ;--->Here we provided our own module begin with a name
                                             ;#%module-begin which is a macro defined below
  ranch)
;Here we provide the module contains module begin function
;which is inverse of importing it
#| ************************************** |#
(require
  (for-syntax
     racket/base             
     syntax/stx
     syntax/parse))
#| Those are the in-built modules of racket we are imported now |#
#| *************************************** |#
;writing a module


(define-syntax-rule (module-begin expr) ;Here macro declares a module name module-begin expr 
  (#%module-begin
    (provide the-ranch)
    (define the-ranch expr))) ;Here we just changed a way of moduleb begin works and this provides has a variable ranch

(define-syntax (ranch stx)
  (syntax-parse stx
    #:datum-literals (ponies pony)
    [(_ (ponies (pony name:id cry:str) ...))
     #'(lambda (pony-name)
         (cond
           [(eq? pony-name 'name) cry] ...
           (else "This pony does not exist!")))]))
;Here whatever we are declaring inside the syntax-rule becomes standard sytem for
;for which seen in result
;and those are called as macros which begins with expression as argument
;Then calling the orginal module which contains a the-ranch and with it's expression's

