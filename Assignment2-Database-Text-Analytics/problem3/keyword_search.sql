select A.docid, sum(A.count * B.count) from AllDocs as A, frequency as B where A.term = B.term and B.term in ('washington', 'taxes', 'treasury') group by A.docid ORDER by sum(A.count * B.count);
