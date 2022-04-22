INSERT INTO [Production].[ProductPhoto] 
([ModifiedDate],[ThumbNailPhoto],[ThumbnailPhotoFileName],[LargePhoto], [LargePhotoFileName])
values ('13.04.2022 17:49:00', 
        (SELECT * FROM OPENROWSET(BULK N'C:\ProductPhotos\helmet_black.gif', SINGLE_BLOB) as T1),
        'helmet_black.gif',
        (SELECT * FROM OPENROWSET(BULK N'C:\ProductPhotos\helmet_black.gif', SINGLE_BLOB) as T1),
        'helmet_black.gif')

INSERT INTO [Production].[ProductPhoto] 
([ModifiedDate],[ThumbNailPhoto],[ThumbnailPhotoFileName],[LargePhoto], [LargePhotoFileName])
values ('13.04.2022 17:49:00', 
        (SELECT * FROM OPENROWSET(BULK N'C:\ProductPhotos\helmet_blue.gif', SINGLE_BLOB) as T1),
        'helmet_blue.gif',
        (SELECT * FROM OPENROWSET(BULK N'C:\ProductPhotos\helmet_blue.gif', SINGLE_BLOB) as T1),
        'helmet_blue.gif')

INSERT INTO [Production].[ProductPhoto] 
([ModifiedDate],[ThumbNailPhoto],[ThumbnailPhotoFileName],[LargePhoto], [LargePhotoFileName])
values ('13.04.2022 17:49:00', 
        (SELECT * FROM OPENROWSET(BULK N'C:\ProductPhotos\awc_cap.gif', SINGLE_BLOB) as T1),
        'awc_cap.gif',
        (SELECT * FROM OPENROWSET(BULK N'C:\ProductPhotos\awc_cap.gif', SINGLE_BLOB) as T1),
        'awc_cap.gif')

INSERT INTO [Production].[ProductPhoto] 
([ModifiedDate],[ThumbNailPhoto],[ThumbnailPhotoFileName],[LargePhoto], [LargePhotoFileName])
values ('13.04.2022 17:49:00', 
        (SELECT * FROM OPENROWSET(BULK N'C:\ProductPhotos\touring_tire.gif', SINGLE_BLOB) as T1),
        'touring_tire.gif',
        (SELECT * FROM OPENROWSET(BULK N'C:\ProductPhotos\touring_tire.gif', SINGLE_BLOB) as T1),
        'touring_tire.gif')

INSERT INTO [Production].[ProductPhoto] 
([ModifiedDate],[ThumbNailPhoto],[ThumbnailPhotoFileName],[LargePhoto], [LargePhotoFileName])
values ('13.04.2022 17:49:00', 
        (SELECT * FROM OPENROWSET(BULK N'C:\ProductPhotos\ml_mountain_tire.gif', SINGLE_BLOB) as T1),
        'ml_mountain_tire.gif',
        (SELECT * FROM OPENROWSET(BULK N'C:\ProductPhotos\ml_mountain_tire.gif', SINGLE_BLOB) as T1),
        'ml_mountain_tire.gif')

INSERT INTO [Production].[ProductPhoto] 
([ModifiedDate],[ThumbNailPhoto],[ThumbnailPhotoFileName],[LargePhoto], [LargePhotoFileName])
values ('13.04.2022 17:49:00', 
        (SELECT * FROM OPENROWSET(BULK N'C:\ProductPhotos\mountain_tire_tube.gif', SINGLE_BLOB) as T1),
        'mountain_tire_tube.gif',
        (SELECT * FROM OPENROWSET(BULK N'C:\ProductPhotos\mountain_tire_tube.gif', SINGLE_BLOB) as T1),
        'mountain_tire_tube.gif')

INSERT INTO [Production].[ProductPhoto] 
([ModifiedDate],[ThumbNailPhoto],[ThumbnailPhotoFileName],[LargePhoto], [LargePhotoFileName])
values ('13.04.2022 17:49:00', 
        (SELECT * FROM OPENROWSET(BULK N'C:\ProductPhotos\ml_road_tire.gif', SINGLE_BLOB) as T1),
        'ml_road_tire.gif',
        (SELECT * FROM OPENROWSET(BULK N'C:\ProductPhotos\ml_road_tire.gif', SINGLE_BLOB) as T1),
        'ml_road_tire.gif')

INSERT INTO [Production].[ProductPhoto] 
([ModifiedDate],[ThumbNailPhoto],[ThumbnailPhotoFileName],[LargePhoto], [LargePhotoFileName])
values ('13.04.2022 17:49:00', 
        (SELECT * FROM OPENROWSET(BULK N'C:\ProductPhotos\road_tire_tube.gif', SINGLE_BLOB) as T1),
        'road_tire_tube.gif',
        (SELECT * FROM OPENROWSET(BULK N'C:\ProductPhotos\road_tire_tube.gif', SINGLE_BLOB) as T1),
        'road_tire_tube.gif')

INSERT INTO [Production].[ProductPhoto] 
([ModifiedDate],[ThumbNailPhoto],[ThumbnailPhotoFileName],[LargePhoto], [LargePhotoFileName])
values ('13.04.2022 17:49:00', 
        (SELECT * FROM OPENROWSET(BULK N'C:\ProductPhotos\mountain_bottle_cage.gif', SINGLE_BLOB) as T1),
        'mountain_bottle_cage.gif',
        (SELECT * FROM OPENROWSET(BULK N'C:\ProductPhotos\mountain_bottle_cage.gif', SINGLE_BLOB) as T1),
        'mountain_bottle_cage.gif')

INSERT INTO [Production].[ProductPhoto] 
([ModifiedDate],[ThumbNailPhoto],[ThumbnailPhotoFileName],[LargePhoto], [LargePhotoFileName])
values ('13.04.2022 17:49:00', 
        (SELECT * FROM OPENROWSET(BULK N'C:\ProductPhotos\helmet_red.gif', SINGLE_BLOB) as T1),
        'helmet_red.gif',
        (SELECT * FROM OPENROWSET(BULK N'C:\ProductPhotos\helmet_red.gif', SINGLE_BLOB) as T1),
        'helmet_red.gif')

-- AB HIER NEUE BILDER -- 22.04.2022 !!!!!!!!!!!!!!

INSERT INTO [Production].[ProductPhoto] 
([ModifiedDate],[ThumbNailPhoto],[ThumbnailPhotoFileName],[LargePhoto], [LargePhotoFileName])
values ('13.04.2022 17:49:00', 
        (SELECT * FROM OPENROWSET(BULK N'C:\ProductPhotos\gloves.gif', SINGLE_BLOB) as T1),
        'gloves.gif',
        (SELECT * FROM OPENROWSET(BULK N'C:\ProductPhotos\gloves.gif', SINGLE_BLOB) as T1),
        'gloves.gif')

INSERT INTO [Production].[ProductPhoto] 
([ModifiedDate],[ThumbNailPhoto],[ThumbnailPhotoFileName],[LargePhoto], [LargePhotoFileName])
values ('13.04.2022 17:49:00', 
        (SELECT * FROM OPENROWSET(BULK N'C:\ProductPhotos\hydration.gif', SINGLE_BLOB) as T1),
        'hydration.gif',
        (SELECT * FROM OPENROWSET(BULK N'C:\ProductPhotos\hydration.gif', SINGLE_BLOB) as T1),
        'hydration.gif')