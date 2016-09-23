(defparameter *nodes* '((living-room (you are in the living room. a wizard is snoring in the couch.))
                        (garden (you are in a beautiful garden. there is a well in front of you.))
                        (attic (you are in the attic. there is a giant welding torch in the corner.))))

(defparameter *edges* '((living-room (garden west door) (attic upstairs ladder))
                        (garden (living-room east door))
                        (attic (living-room downstairs ladder))))



(defparameter *max-label-length* 30)

(defun dot-name (string)
  (substitute-if #\_ (complement #'alphanumericp) (prin1-to-string string)))

(defun dot-label (string)
  (if string
    (let ((s (write-to-string string :pretty nil)))
      (if (> (length s) *max-label-length*)
        (concatenate 'string (subseq s 0 (- *max-label-length* 3)) "...")
        s))
        ""))

(defun nodes-to-dot (nodes)
  (mapc (lambda (node)
    (fresh-line)
    (princ (dot-name (car node)))
    (princ "[label=\"")
    (princ (dot-label node))
    (princ "\"];")) nodes))

(defun edges-to-dot (edges)
  (mapc (lambda (node)
    (mapc (lambda (edge)
        (fresh-line)
        (princ (dot-name (car node)))
        (princ "->")
        (princ (dot-name (car edge)))
        (princ "[label=\"")
        (princ (dot-label (cdr edge)))
        (princ "\"];"))
        (cdr node)))
      edges))

(defun graph-to-dot (nodes edges)
  (princ "digraph{")
  (nodes-to-dot nodes)
  (edges-to-dot edges)
  (princ "}"))

(defun ugraph-to-dot (nodes edges)
  (princ "graph{")
  (nodes-to-dot nodes)
  (uedges-to-dot edges)
  (princ "}"))

(defun dot-to-png (fname thunk)
  (with-open-file (*standard-output* fname :direction :output :if-exists :supersede)
    (funcall thunk))
    (ext:shell (concatenate 'string "dot -Tpng -O " fname)))

(defun graph-to-png (fname nodes edges)
  (dot-to-png fname (lambda ()
    (graph-to-dot nodes edges))))

(defun uedges-to-dot (edges)
  (maplist (lambda (lst)
    (mapc (lambda (edge)
      (unless (assoc (car edge) (cdr lst)) (cdr lst))
      (fresh-line)
      (princ (dot-name (caar lst)))
      (princ "--")
      (princ (dot-name (car edge)))
      (princ "[label=\"")
      (princ (dot-label (cdr edge)))
      (princ "\"];"))
      (cdar lst)))
      edges))

(defun ugraph-to-png (fname nodes edges)
  (dot-to-png fname (lambda ()
    (ugraph-to-dot nodes edges))))















