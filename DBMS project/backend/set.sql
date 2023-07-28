select loginid from Authentication union select loginid from Staff;

select staffid from Reader where staffid in (select staffid from Staff);

select loginid from Staff where loginid in (select loginid from Authentication);

select loginid from Staff where loginid not in (select loginid from Authentication);


