CREATE TABLE [dbo].[fids] (
  [origin] nvarchar(50) COLLATE SQL_Latin1_General_CP1_CI_AS  NOT NULL,
  [destination] nvarchar(50) COLLATE SQL_Latin1_General_CP1_CI_AS  NOT NULL,
  [register] nvarchar(50) COLLATE SQL_Latin1_General_CP1_CI_AS  NOT NULL,
  [flight_num] nvarchar(50) COLLATE SQL_Latin1_General_CP1_CI_AS  NOT NULL,
  [airplane] nvarchar(50) COLLATE SQL_Latin1_General_CP1_CI_AS  NULL,
  [scheduled_date] nvarchar(50) COLLATE SQL_Latin1_General_CP1_CI_AS  NOT NULL,
  [scheduled_time] time(7)  NOT NULL,
  [actual_date] nvarchar(50) COLLATE SQL_Latin1_General_CP1_CI_AS  NULL,
  [actual_time] time(7)  NULL,
  [airline_icao] nvarchar(50) COLLATE SQL_Latin1_General_CP1_CI_AS  NOT NULL,
  [international] bit  NOT NULL,
  [delay_] int  NULL,
  [type_] nvarchar(50) COLLATE SQL_Latin1_General_CP1_CI_AS  NOT NULL,
  [miladi_scheduled] date  NOT NULL,
  [miladi_actual] date  NULL,
  [id] int  IDENTITY(1,1) NOT NULL,
  [airline] nvarchar(50) COLLATE SQL_Latin1_General_CP1_CI_AS  NOT NULL
)
GO