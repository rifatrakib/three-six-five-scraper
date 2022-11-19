from datetime import datetime
from typing import List, Union

from pydantic import BaseModel


class Instructor(BaseModel):
    name: str
    slug: str


class LessonStatus(BaseModel):
    completed: int
    total: int


class ReviewStatus(BaseModel):
    courseId: int
    rating: float
    ratings: int


class CourseBase(BaseModel):
    completedLessons: int
    duration: int
    instructors: str
    lessons: LessonStatus
    name: str
    progress: int
    slug: str
    smallImage: str
    technology: str


class Course(CourseBase):
    key: str = "courses"
    bigImage: str
    certificateNumber: Union[str, None] = None
    completed: Union[datetime, None] = None
    created: datetime
    examId: Union[int, None] = None
    id: int
    instructorsArr: List[Instructor] = []
    instructorsSlugs: str
    latestCompleted: Union[datetime, None] = None
    moduleId: int
    moduleName: str
    popular: bool
    reviews: Union[ReviewStatus, None] = None
    shortDescription: str
    started: Union[datetime, None] = None
    status: str
    topic: str
    unlocked: bool


class Module(BaseModel):
    key: str = "modules"
    businessDescription: str
    description: str
    id: int
    name: str
    slug: str


class Page(BaseModel):
    key: str = "page"
    canonicalUrl: Union[str, None] = None
    content: str
    created: datetime
    id: int
    metaDescription: str
    metaImage: Union[str, None] = None
    metaKeywords: Union[str, None] = None
    metaTitle: str
    ogDescription: Union[str, None] = None
    ogImage: Union[str, None] = None
    ogTitle: Union[str, None] = None
    robots: Union[str, None] = None
    title: str
    twitterDescription: Union[str, None] = None
    twitterImage: Union[str, None] = None
    twitterTitle: Union[str, None] = None
    updated: datetime
    url: str
    visible: bool


class RecommendationCourse(CourseBase):
    courseId: int
    description: str
    image: str


class RecommendationTrack(BaseModel):
    certificateNumber: Union[str, None] = None
    completed: Union[datetime, None] = None
    completedCourses: int
    description: str
    enrolled: Union[bool, None] = None
    hoursOfVideo: int
    id: int
    name: str
    progress: int
    slug: str
    totalCourses: int


class Recommendation(BaseModel):
    key: str = "recommendations"
    courses: List[RecommendationCourse]
    track: RecommendationTrack


class UpcomingCourse(BaseModel):
    key: str = "upcoming"
    active: bool
    created: datetime
    description: str
    duration: int
    id: int
    instructor: str
    instructorPhoto: str
    launchDate: datetime
    lessons: int
    name: str
    slug: str
    technology: str
