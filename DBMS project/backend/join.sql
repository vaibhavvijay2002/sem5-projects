select s.staffid,s.staffname from Staff as s inner join Report as r where s.staffid = r.staffid;

select s.staffid,s.staffname from Staff as s inner join Reader as r where s.staffid = r.staffid;

select b.ISBN,p.publishername from Book as b left outer join Publisher as p on b.publisherid = p.publisherid;

select s.loginid,a.password from Staff as s left outer join Authentication as a on s.loginid = a.loginid;