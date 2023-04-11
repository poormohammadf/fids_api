with fids_temp as
(SELECT cast(miladi_scheduled as datetime) + cast(scheduled_time as datetime) scheduled_datetime, cast(miladi_actual as datetime) + cast(actual_time as datetime) actual_datetime,*
from fids
)

select  DATEDIFF(minute, scheduled_datetime, actual_datetime) delay,delay_,*
from fids_temp
where DATEDIFF(minute, scheduled_datetime, actual_datetime) <> delay_
order by delay

SELECT sum(case when delay_ < 0 then delay_ end) haste,sum(case when delay_ >=0 then delay_ end) delay,airline
from fids 
GROUP BY airline