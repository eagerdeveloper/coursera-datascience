select distinct docid from frequency
where term = 'world' and docid in (select distinct docid from frequency where term = 'transaction');
