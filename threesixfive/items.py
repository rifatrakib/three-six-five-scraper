from datetime import datetime
from typing import List, Union

from pydantic import BaseModel, HttpUrl


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


class DownloadableAsset(BaseModel):
    name: str
    file: str


class VideoInfo(BaseModel):
    duration: int
    durationSeconds: float
    extId: str
    id: int
    name: str
    provider: str


class Asset(BaseModel):
    key: str = "asset"
    assignment: Union[bool, None] = None
    cases: Union[int, None] = None
    completed: Union[bool, None] = None
    course_name: str
    chapter_id: int
    chapter_name: str
    chapter_order: int
    downloadables: List[DownloadableAsset] = []
    duration: Union[int, None] = None
    free: bool
    id: int
    lectureId: Union[int, None] = None
    name: str
    order: Union[str, None] = None
    practiceExam: Union[bool, None] = None
    quiz: Union[bool, None] = None
    questions: Union[int, None] = None
    review: Union[bool, None] = None
    section: int
    slug: Union[str, None] = None
    type: Union[str, None] = None
    text: Union[str, None] = None
    unlocked: Union[bool, None] = None
    usefulOrNot: Union[bool, None] = None
    video: Union[VideoInfo, bool, None] = None


class MediaSource(BaseModel):
    key: str = "media"
    course_name: str
    chapter_name: str
    lesson_name: str
    avg_bitrate: Union[int, None] = None
    codecs: Union[str, None] = None
    container: Union[str, None] = None
    duration: Union[int, None] = None
    height: Union[int, None] = None
    profiles: Union[str, None] = None
    size: Union[int, None] = None
    src: HttpUrl
    type: Union[str, None] = None
    width: Union[int, None] = None
    subtitle: Union[HttpUrl, None] = None
