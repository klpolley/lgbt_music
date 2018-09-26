create table Artist (
  id        integer primary key autoincrement,
  name      varchar(128) not null,
  hometown  varchar(128),
  countryID integer not null,
  foreign key (countryID) references Country(id)
);

create table Event (
  id        integer primary key autoincrement,
  name      varchar(128) not null,
  date      varchar(64) not null,
  venueID   integer not null,
  foreign key (venueID) references Venue(id)
);

create table ArtistToEvent (
  id        integer primary key autoincrement,
  artistID  integer not null,
  eventID   integer not null,
  foreign key (artistID) references Artist(id),
  foreign key (eventID) references Event(id)
);

create table Venue (
  id        integer primary key autoincrement,
  name      varchar(128) not null,
  city      varchar(64) not null,
  countryID integer not null,
  foreign key (countryID) references Country(id)
);

create table Country (
  id        integer primary key autoincrement,
  name      varchar(128) not null,
  abbr      varchar(16),
);

create table Genre (
  id        integer primary key autoincrement,
  name      varchar(64) not null,
  abbr      varchar(16),
);

create table ArtistToGenre (
  id        integer primary key autoincrement,
  artistID  integer not null,
  genreID   integer not null,
  foreign key (artistID) references Artist(id),
  foreign key (genreID) references Genre(id)
)
