class Article:
    def __init__(self, author, magazine, title):
        if not isinstance(title, str) or len(title) < 5 or len(title) > 50:
            raise ValueError("Title must be a string of length between 5 and 50 characters.")
        self._author = author
        self._magazine = magazine
        self._title = title

    @property
    def title(self):
        return self._title

    @property
    def author(self):
        return self._author

    @property
    def magazine(self):
        return self._magazine


class Author:
    def __init__(self, name):
        if not isinstance(name, str) or len(name) == 0:
            raise ValueError("Name must be a non-empty string.")
        self._name = name
        self._articles = []  # Store articles written by the author

    @property
    def name(self):
        return self._name

    def articles(self):
        return self._articles

    def magazines(self):
        return list(set(article.magazine for article in self._articles))

    def add_article(self, magazine, title):
        article = Article(self, magazine, title)
        self._articles.append(article)
        magazine._articles.append(article)  # Associate article with the magazine
        return article

    def topic_areas(self):
        topic_areas = list(set(magazine.category for magazine in self.magazines()))
        return topic_areas if topic_areas else None


class Magazine:
    _all_magazines = []  # Class variable to keep track of all magazine instances

    def __init__(self, name, category):
        if not isinstance(name, str) or len(name) < 2 or len(name) > 16:
            raise ValueError("Name must be a string of length between 2 and 16 characters.")
        if not isinstance(category, str) or len(category) == 0:
            raise ValueError("Category must be a non-empty string.")
        self._name = name
        self._category = category
        self._articles = []  # Store articles published in the magazine
        Magazine._all_magazines.append(self)  # Register this magazine in the class variable

    @property
    def name(self):
        return self._name

    @property
    def category(self):
        return self._category

    def articles(self):
        return self._articles

    def contributors(self):
        return list(set(article.author for article in self._articles))

    def article_titles(self):
        return [article.title for article in self._articles]  

    def contributing_authors(self):
        author_counts = {}
        for article in self._articles:
            if article.author not in author_counts:
                author_counts[article.author] = 0
            author_counts[article.author] += 1
        contributing_authors = [author for author, count in author_counts.items() if count > 2]
        return contributing_authors if contributing_authors else []  

    @classmethod
    def top_publisher(cls):
        if not cls._all_magazines:
            return None
        return max(cls._all_magazines, key=lambda magazine: len(magazine.articles())) or None

    @classmethod
    def get_magazine_by_name(cls, name):
        for magazine in cls._all_magazines:
            if magazine.name == name:
                return magazine
        return None

    @classmethod
    def get_all_magazines(cls):
        return cls._all_magazines

class Article:
    def __init__(self, author, magazine, title):
        if not isinstance(title, str) or len(title) < 5 or len(title) > 50:
            raise ValueError("Title must be a string of length between 5 and 50 characters.")
        self._author = author
        self._magazine = magazine
        self._title = title

    @property
    def title(self):
        return self._title

    @property
    def author(self):
        return self._author

    @property
    def magazine(self):
        return self._magazine

  