(defvar *max* 100)
(defvar *min* 1)

(defun guess()
    (ash (+ *max* *min*) -1))


(defun smaller()
    (setq *max* (1- (guess)))
    (guess))


(defun bigger()
    (setq *min* (1+ (guess)))
    (guess))


(defun reset()
    (setq *max* 100)
    (setq *min* 0)
    (guess))
