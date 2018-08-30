-- 静态网站
-- 1.中国观鸟中心 china_observ_birds_recordcenter、china_observ_birds_recordcenter_watchrecord（旧版china_recordlist4field china_watchrecord4field）
-- 2.ebird ebird_checklist、ebird_record
-- 3.gbif（其余以gbif开头的均为测试表）
-- 4.movebank
-- 5.seamap（文件字段不唯一、未创建）

CREATE TABLE `china_observ_birds_recordcenter` (
  `id` varchar(255) NOT NULL,
  `seq` varchar(13) NOT NULL COMMENT '序号',
  `observ_time` varchar(25) NOT NULL COMMENT '观测时间',
  `observ_site` varchar(200) NOT NULL COMMENT '观测地点',
  `bird_species` int(5) NOT NULL COMMENT '鸟种数',
  `recorder` varchar(20) NOT NULL COMMENT '记录者',
  `browse_count` int(10) NOT NULL COMMENT '浏览数',
  `create_time` datetime NOT NULL COMMENT '入库时间',
  `update_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

CREATE TABLE `china_observ_birds_recordcenter_watchrecord` (
  `id` varchar(255) NOT NULL,
  `birds_name` varchar(5000) DEFAULT NULL COMMENT '鸟种名字',
  `update_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

CREATE TABLE `china_recordlist4field` (
  `id` varchar(255) NOT NULL,
  `seq` varchar(255) NOT NULL COMMENT '序号',
  `observ_site` varchar(255) NOT NULL COMMENT '观测地点',
  `bird_species` varchar(255) NOT NULL COMMENT '鸟种数',
  `recorder` varchar(255) NOT NULL COMMENT '记录者',
  `browse_count` varchar(255) NOT NULL COMMENT '浏览数',
  `create_time` varchar(255) NOT NULL COMMENT '入库时间',
  `update_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

CREATE TABLE `china_watchrecord4field` (
  `id` varchar(255) NOT NULL,
  `birds_name` varchar(10000) DEFAULT NULL COMMENT '鸟种名字',
  `observ_time` varchar(255) DEFAULT NULL,
  `update_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

CREATE TABLE `ebird_checklist` (
  `species_href` varchar(255) DEFAULT NULL,
  `species_time` varchar(255) DEFAULT NULL,
  `species_date_effort` varchar(5000) DEFAULT NULL,
  `update_time` timestamp NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `species_protocol` varchar(255) DEFAULT NULL,
  `species_party_size` varchar(255) DEFAULT NULL,
  `species_duration` varchar(255) DEFAULT NULL,
  `species_distance` varchar(255) DEFAULT NULL,
  `species_observers` varchar(255) DEFAULT NULL,
  `species_comments` varchar(255) DEFAULT NULL,
  `species_version` varchar(255) DEFAULT NULL,
  `species_total` text
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

CREATE TABLE `ebird_record` (
  `species_id` varchar(255) DEFAULT NULL,
  `species_name` varchar(255) NOT NULL,
  `species_count` varchar(255) DEFAULT NULL,
  `species_date` varchar(255) DEFAULT NULL,
  `species_by` varchar(255) DEFAULT NULL,
  `species_href` varchar(255) NOT NULL,
  `species_loc` varchar(255) DEFAULT NULL,
  `species_country` varchar(255) DEFAULT NULL,
  `update_time` timestamp NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`species_href`,`species_name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

CREATE TABLE `gbif` (
  `ID` int(11) NOT NULL AUTO_INCREMENT,
  `key_1` varchar(255) NOT NULL DEFAULT '',
  `datasetKey` varchar(255) DEFAULT NULL,
  `publishingOrgKey` varchar(255) DEFAULT NULL,
  `publishingCountry` varchar(255) DEFAULT NULL,
  `protocol` varchar(255) DEFAULT NULL,
  `lastCrawled` varchar(255) DEFAULT NULL,
  `lastParsed` varchar(255) DEFAULT NULL,
  `crawlId` varchar(255) DEFAULT NULL,
  `extensions` varchar(255) DEFAULT NULL,
  `basisOfRecord` varchar(255) DEFAULT NULL,
  `taxonKey` varchar(255) DEFAULT NULL,
  `kingdomKey` varchar(255) DEFAULT NULL,
  `phylumKey` varchar(255) DEFAULT NULL,
  `classKey` varchar(255) DEFAULT NULL,
  `orderKey` varchar(255) DEFAULT NULL,
  `familyKey` varchar(255) DEFAULT NULL,
  `genusKey` varchar(255) DEFAULT NULL,
  `speciesKey` varchar(255) DEFAULT NULL,
  `scientificName` varchar(255) DEFAULT NULL,
  `kingdom` varchar(255) DEFAULT NULL,
  `phylum` varchar(255) DEFAULT NULL,
  `order_1` varchar(255) DEFAULT NULL,
  `family` varchar(255) DEFAULT NULL,
  `genus` varchar(255) DEFAULT NULL,
  `species` varchar(255) DEFAULT NULL,
  `genericName` varchar(255) DEFAULT NULL,
  `specificEpithet` varchar(255) DEFAULT NULL,
  `taxonRank` varchar(255) DEFAULT NULL,
  `dateIdentified` varchar(255) DEFAULT NULL,
  `decimalLongitude` varchar(255) DEFAULT NULL,
  `decimalLatitude` varchar(255) DEFAULT NULL,
  `coordinateUncertaintyInMeters` varchar(255) DEFAULT NULL,
  `year_1` varchar(255) DEFAULT NULL,
  `month_1` varchar(255) DEFAULT NULL,
  `day_1` varchar(255) DEFAULT NULL,
  `eventDate` varchar(255) DEFAULT NULL,
  `issues` varchar(255) DEFAULT NULL,
  `modified` varchar(255) DEFAULT NULL,
  `lastInterpreted` varchar(255) DEFAULT NULL,
  `references_1` varchar(255) DEFAULT NULL,
  `license` varchar(255) DEFAULT NULL,
  `identifiers` varchar(255) DEFAULT NULL,
  `media` text,
  `facts` varchar(255) DEFAULT NULL,
  `relations` varchar(255) DEFAULT NULL,
  `geodeticDatum` varchar(255) DEFAULT NULL,
  `class_1` varchar(255) DEFAULT NULL,
  `countryCode` varchar(255) DEFAULT NULL,
  `country` varchar(255) DEFAULT NULL,
  `rightsHolder` varchar(255) DEFAULT NULL,
  `identifier` varchar(255) DEFAULT NULL,
  `informationWithheld` varchar(255) DEFAULT NULL,
  `verbatimEventDate` varchar(255) DEFAULT NULL,
  `datasetName` varchar(255) DEFAULT NULL,
  `gbifID` varchar(255) DEFAULT NULL,
  `collectionCode` varchar(255) DEFAULT NULL,
  `verbatimLocality` varchar(255) DEFAULT NULL,
  `occurrenceID` varchar(255) DEFAULT NULL,
  `taxonID` varchar(255) DEFAULT NULL,
  `catalogNumber` varchar(255) DEFAULT NULL,
  `recordedBy` varchar(255) DEFAULT NULL,
  `http_unknown_org_occurrenceDetails` varchar(255) DEFAULT NULL,
  `institutionCode` varchar(255) DEFAULT NULL,
  `rights` varchar(255) DEFAULT NULL,
  `eventTime` varchar(255) DEFAULT NULL,
  `identificationID` varchar(255) DEFAULT NULL,
  `_datasetKey` varchar(255) DEFAULT NULL,
  `_publishingOrgKey` varchar(255) DEFAULT NULL,
  `_verbatimRecord` varchar(255) DEFAULT NULL,
  `scrapy_country` varchar(255) DEFAULT NULL,
  `update_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`ID`,`key_1`),
  KEY `index_year_1` (`year_1`) USING BTREE,
  KEY `index_month_1` (`month_1`) USING BTREE,
  KEY `index_scrapy_country` (`scrapy_country`) USING BTREE
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

CREATE TABLE `movebank` (
  `event_id` varchar(255) DEFAULT NULL,
  `visible` varchar(255) DEFAULT NULL,
  `timestamp` varchar(255) DEFAULT NULL,
  `location_long` varchar(255) DEFAULT NULL,
  `location_lat` varchar(255) DEFAULT NULL,
  `ground_speed` varchar(255) DEFAULT NULL,
  `heading` varchar(255) DEFAULT NULL,
  `height_above_ellipsoid` varchar(255) DEFAULT NULL,
  `sensor_type` varchar(255) DEFAULT NULL,
  `individual_taxon_canonical_name` varchar(255) DEFAULT NULL,
  `tag_local_identifier` varchar(255) DEFAULT NULL,
  `individual_local_identifier` varchar(255) DEFAULT NULL,
  `study_name` varchar(255) DEFAULT NULL,
  `update_time` timestamp NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=utf8;



-- 动态网站
-- 1.德鲁伊 druid_technology_behavior、druid_technology_gps
-- 2.ecotone
-- 3.hqxs
-- 4.koeco
-- 5.ornitela

CREATE TABLE `druid_technology_behavior` (
  `id` varchar(255) NOT NULL,
  `device_id` varchar(255) DEFAULT NULL,
  `company_id` varchar(255) DEFAULT NULL,
  `company_name` varchar(255) DEFAULT NULL,
  `uuid` varchar(255) DEFAULT NULL,
  `firmware_version` varchar(255) DEFAULT NULL,
  `timestamp` varchar(255) DEFAULT NULL,
  `updated_at` varchar(255) DEFAULT NULL,
  `mark` varchar(255) DEFAULT NULL,
  `sleep_time` varchar(255) DEFAULT NULL,
  `other_time` varchar(255) DEFAULT NULL,
  `activity_time` varchar(255) DEFAULT NULL,
  `fly_time` varchar(255) DEFAULT NULL,
  `peck_time` varchar(255) DEFAULT NULL,
  `crawl_time` varchar(255) DEFAULT NULL,
  `run_time` varchar(255) DEFAULT NULL,
  `total_expend` varchar(255) DEFAULT NULL,
  `sleep_expend` varchar(255) DEFAULT NULL,
  `other_expend` varchar(255) DEFAULT NULL,
  `activity_expend` varchar(255) DEFAULT NULL,
  `fly_expend` varchar(255) DEFAULT NULL,
  `peck_expend` varchar(255) DEFAULT NULL,
  `crawl_expend` varchar(255) DEFAULT NULL,
  `run_expend` varchar(255) DEFAULT NULL,
  `update_time` timestamp NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

CREATE TABLE `druid_technology_gps` (
  `id` varchar(255) NOT NULL,
  `device_id` varchar(255) DEFAULT NULL,
  `company_id` varchar(255) DEFAULT NULL,
  `company_name` varchar(255) DEFAULT NULL,
  `mark` varchar(255) DEFAULT NULL,
  `uuid` varchar(255) DEFAULT NULL,
  `firmware_version` varchar(255) DEFAULT NULL,
  `updated_at` varchar(255) DEFAULT NULL,
  `timestamp` varchar(255) DEFAULT NULL,
  `sms` varchar(255) DEFAULT NULL,
  `longitude` varchar(255) DEFAULT NULL,
  `latitude` varchar(255) DEFAULT NULL,
  `altitude` varchar(255) DEFAULT NULL,
  `temperature` varchar(255) DEFAULT NULL,
  `humidity` varchar(255) DEFAULT NULL,
  `light` varchar(255) DEFAULT NULL,
  `pressure` varchar(255) DEFAULT NULL,
  `used_star` varchar(255) DEFAULT NULL,
  `view_star` varchar(255) DEFAULT NULL,
  `dimension` varchar(255) DEFAULT NULL,
  `speed` varchar(255) DEFAULT NULL,
  `horizontal` varchar(255) DEFAULT NULL,
  `vertical` varchar(255) DEFAULT NULL,
  `course` varchar(255) DEFAULT NULL,
  `battery_voltage` varchar(255) DEFAULT NULL,
  `signal_strength` varchar(255) DEFAULT NULL,
  `point_location` varchar(255) DEFAULT NULL,
  `fix_time` varchar(255) DEFAULT NULL,
  `update_time` timestamp NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

CREATE TABLE `ecotone` (
  `gps_pos_csv` varchar(255) DEFAULT NULL,
  `idnr` varchar(255) DEFAULT NULL,
  `gpsnumber` varchar(255) DEFAULT NULL,
  `gpstime` varchar(255) DEFAULT NULL,
  `smstime` varchar(255) DEFAULT NULL,
  `latitude` varchar(255) DEFAULT NULL,
  `longtitude` varchar(255) DEFAULT NULL,
  `batteryvoltage` varchar(255) DEFAULT NULL,
  `gpsdescription` varchar(255) DEFAULT NULL,
  `temperature` varchar(255) DEFAULT NULL,
  `gpsintervals` varchar(255) DEFAULT NULL,
  `vhftelemetry` varchar(255) DEFAULT NULL,
  `activity` varchar(255) DEFAULT NULL,
  `gsmsignal` varchar(255) DEFAULT NULL,
  `n_satellites` varchar(255) DEFAULT NULL,
  `speed_knots` varchar(255) DEFAULT NULL,
  `altitude` varchar(255) DEFAULT NULL,
  `light` varchar(255) DEFAULT NULL,
  `acc_x` varchar(255) DEFAULT NULL,
  `acc_y` varchar(255) DEFAULT NULL,
  `acc_z` varchar(255) DEFAULT NULL,
  `update_time` timestamp NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

CREATE TABLE `hqxs` (
  `terminal` varchar(255) DEFAULT NULL,
  `imeid` varchar(255) DEFAULT NULL,
  `time` varchar(255) DEFAULT NULL,
  `ew` varchar(255) DEFAULT NULL,
  `longitude` varchar(255) DEFAULT NULL,
  `ns` varchar(255) DEFAULT NULL,
  `latitude` varchar(255) DEFAULT NULL,
  `speed` varchar(255) DEFAULT NULL,
  `course` varchar(255) DEFAULT NULL,
  `altitude` varchar(255) DEFAULT NULL,
  `temperature` varchar(255) DEFAULT NULL,
  `voltage` varchar(255) DEFAULT NULL,
  `exercise` varchar(255) DEFAULT NULL,
  `satellites` varchar(255) DEFAULT NULL,
  `hdop` varchar(255) DEFAULT NULL,
  `vdop` varchar(255) DEFAULT NULL,
  `precisiongrade` varchar(255) DEFAULT NULL,
  `update_time` timestamp NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

CREATE TABLE `koeco` (
  `seq` varchar(255) NOT NULL,
  `tracker_id` varchar(255) DEFAULT NULL,
  `date_utc` varchar(255) DEFAULT NULL,
  `date_kst` varchar(255) DEFAULT NULL,
  `decimal_latitude` varchar(255) DEFAULT NULL,
  `decimal_longitude` varchar(255) DEFAULT NULL,
  `dms_latitude` varchar(255) DEFAULT NULL,
  `dms_longitude` varchar(255) DEFAULT NULL,
  `altitude` varchar(255) DEFAULT NULL,
  `heading` varchar(255) DEFAULT NULL,
  `speed` varchar(255) DEFAULT NULL,
  `satellite` varchar(255) DEFAULT NULL,
  `fixed_level` varchar(255) DEFAULT NULL,
  `dop` varchar(255) DEFAULT NULL,
  `contact_time` varchar(255) DEFAULT NULL,
  `volt` varchar(255) DEFAULT NULL,
  `update_time` timestamp NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`seq`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

CREATE TABLE `ornitela` (
  `device_id` varchar(255) DEFAULT NULL,
  `utc_datetime` varchar(255) DEFAULT NULL,
  `utc_date1` varchar(255) DEFAULT NULL,
  `utc_time1` varchar(255) DEFAULT NULL,
  `datatype` varchar(255) DEFAULT NULL,
  `satcount` varchar(255) DEFAULT NULL,
  `u_bat_mv` varchar(255) DEFAULT NULL,
  `bat_soc_pct` varchar(255) DEFAULT NULL,
  `solar_i_ma` varchar(255) DEFAULT NULL,
  `hdop` varchar(255) DEFAULT NULL,
  `latitude` varchar(255) DEFAULT NULL,
  `longitude` varchar(255) DEFAULT NULL,
  `altitude_m` varchar(255) DEFAULT NULL,
  `speed_km_h` varchar(255) DEFAULT NULL,
  `direction_deg` varchar(255) DEFAULT NULL,
  `temperature_c` varchar(255) DEFAULT NULL,
  `light` varchar(255) DEFAULT NULL,
  `mag_x` varchar(255) DEFAULT NULL,
  `mag_y` varchar(255) DEFAULT NULL,
  `mag_z` varchar(255) DEFAULT NULL,
  `acc_x` varchar(255) DEFAULT NULL,
  `acc_y` varchar(255) DEFAULT NULL,
  `acc_z` varchar(255) DEFAULT NULL,
  `update_time` timestamp NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- 数仓BS层表设计（表合并）

CREATE TABLE `bs_mix_source_info` (
  `UUID` varchar(255) DEFAULT NULL,
  `Timestamp` varchar(255) DEFAULT NULL,
  `Latitude` varchar(255) DEFAULT NULL,
  `Longitude` varchar(255) DEFAULT NULL,
  `Altitude` varchar(255) DEFAULT NULL,
  `BatteryVoltage` varchar(255) DEFAULT NULL,
  `Course` varchar(255) DEFAULT NULL,
  `DruidHumidity` varchar(255) DEFAULT NULL,
  `DruidLight` varchar(255) DEFAULT NULL,
  `DruidPressure` varchar(255) DEFAULT NULL,
  `DruidUsedStar` varchar(255) DEFAULT NULL,
  `DruidViewstar` varchar(255) DEFAULT NULL,
  `DruidDimension` varchar(255) DEFAULT NULL,
  `DruidSpeed` varchar(255) DEFAULT NULL,
  `DruidHorizontal` varchar(255) DEFAULT NULL,
  `DruidVertical` varchar(255) DEFAULT NULL,
  `DruidSignalStrength` varchar(255) DEFAULT NULL,
  `EcoGPSIntervals` varchar(255) DEFAULT NULL,
  `EcoVHFTelemetry` varchar(255) DEFAULT NULL,
  `EcoActivity` varchar(255) DEFAULT NULL,
  `EcoGSMSignal` varchar(255) DEFAULT NULL,
  `HQXSSpeed` varchar(255) DEFAULT NULL,
  `HQXSPresciesonGrade` varchar(255) DEFAULT NULL,
  `VetchSpeed` varchar(255) DEFAULT NULL,
  `VetchRadioStrength` varchar(255) DEFAULT NULL,
  `VetchFixedLevel` varchar(255) DEFAULT NULL,
  `VetchDOP` varchar(255) DEFAULT NULL,
  `VetchContactTIme` varchar(255) DEFAULT NULL,
  `VetchVersin` varchar(255) DEFAULT NULL,
  `etl_update_time` timestamp NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

