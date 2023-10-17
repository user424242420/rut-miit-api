import requests_cache


class rutApi():
    def __init__(self, name_cache="rut_miit_cache",
                 backend="sqlite",
                 expire_after=60, *args, **kwargs):
        self.session = requests_cache.CachedSession(name_cache, backend,
                                                    expire_after=expire_after)
        super(self.__class__, self).__init__(*args, **kwargs)

    def getGroupsCatalog(self) -> dict:
        """
        Return list of groups
        """

        return self.session.get(
            "https://rut-miit.ru/data-service/data/timetable/groups-catalog"
        ).json()

    def getGroupsTimetable(self, groupId: int, actualOnly: bool = True,
                           date: None | str = None) -> dict:
        """
        Return timetable of grouos
        data format: 2023-09-01
        """

        return self.session.get(
            f"https://rut-miit.ru/api/v1/public/timetable/v2/group/"
            f"{groupId}/{'d=' + date + ';' if date else ''}"
            f"t=1?actualOnly={str(actualOnly).lower()}"""
        ).json()

    def getPersonTimetable(self, personId: int, actualOnly: bool = True,
                           date: None | str = None):
        """
        Return timetable of grouos
        data format: 2023-09-01
        """

        return self.session.get(
            f"https://rut-miit.ru/api/v1/public/timetable/v2/person/"
            f"{personId}/{'d=' + date + ';' if date else ''}"
            f"t=1?actualOnly={str(actualOnly).lower()}"
        ).json()

    def getNewsCategories(self,
                          idk_information_category: int = 2, id_lang: int = 1):
        """
        Get news
        Other arguments doesnt get anything
        """

        return self.session.get(
            "https://rut-miit.ru/data-service/data/news-categories?"
            f"idk_information_category={idk_information_category}"
            f"&id_lang={id_lang}"
        ).json()

    def getNewsList(self, category_id: int, news_from: int = 1,
                    news_to: int = 1, idk_information_category: int = 2,
                    id_lang: int = 1,  page_size: int = 40):
        """
        Get news list
        category_id: int - list in getNewsCategories
        page_zise: int - count of output
        Other parametrs unknown and undetected
        """

        return self.session.get(
            "https://rut-miit.ru/data-service/data/news?"
            f"from={news_from}&to={news_to}"
            f"&idk_information_category={idk_information_category}"
            f"&id_lang={id_lang}&page_size={page_size}"
            f"&category_id={category_id}"
        ).json()

    def getNews(self, news_id: int):
        """
        Get news by news_id
        Nice html view here https://rut-miit.ru/news/{news_id}/content
        """
        return self.session.get(
            f"https://rut-miit.ru/data-service/data/news/{news_id}"
        ).json()
