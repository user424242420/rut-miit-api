from rut_miit_api import rutApi
import logging
obj = rutApi()
logger = logging.getLogger(__name__)


def test_groups_catalog():
    global obj
    groups = obj.getGroupsCatalog()
    assert groups != {}


def test_groups_catalog_timetable():
    global obj
    groups_timetable = obj.getGroupsTimetable(189996)
    logger.info(groups_timetable)
    assert groups_timetable != {}
    groups_timetable = obj.getGroupsTimetable(
        groupId=189996, date="2023-09-01")
    logger.info(groups_timetable)
    assert groups_timetable != {}


def test_person_timetable():
    global obj
    person_timetable = obj.getPersonTimetable(2241)
    logger.info(person_timetable)
    assert person_timetable != {}
    person_timetable = obj.getPersonTimetable(2241, date="2023-09-01")
    logger.info(person_timetable)
    assert person_timetable != {}


def test_news():
    global obj
    news_categories = obj.getNewsCategories()
    logger.info(news_categories)
    news_list = obj.getNewsList(news_categories[-1]["id"])
    logger.info(news_list)
    news_obj = obj.getNews(news_list["items"][0]["idInformation"])
    logger.info(news_obj)
