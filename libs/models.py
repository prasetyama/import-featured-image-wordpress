# coding: utf-8
from sqlalchemy import BINARY, CHAR, Column, Date, DateTime, Enum, Float, ForeignKey, Index, LargeBinary, String, TIMESTAMP, Table, Text, VARBINARY, text
from sqlalchemy.dialects.mysql import BIGINT, DATETIME, INTEGER, LONGBLOB, LONGTEXT, MEDIUMINT, MEDIUMTEXT, SMALLINT, TINYBLOB, TINYINT, TINYTEXT, VARCHAR
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class AffiliateCategory(Base):
    __tablename__ = 'affiliate_category'

    id = Column(BIGINT(20), primary_key=True)
    reference = Column(ForeignKey('affiliate_category.id'), index=True)
    name = Column(String(255, 'utf8_unicode_ci'), nullable=False)
    is_active = Column(TINYINT(1), nullable=False)
    created_at = Column(DateTime, nullable=False)
    created_by = Column(String(100, 'utf8_unicode_ci'), nullable=False)
    updated_at = Column(DateTime)
    updated_by = Column(String(100, 'utf8_unicode_ci'))

    parent = relationship('AffiliateCategory', remote_side=[id])


class AuthGroup(Base):
    __tablename__ = 'auth_group'

    id = Column(INTEGER(11), primary_key=True)
    name = Column(String(150), nullable=False, unique=True)


class AuthUser(Base):
    __tablename__ = 'auth_user'

    id = Column(INTEGER(11), primary_key=True)
    password = Column(String(128), nullable=False)
    last_login = Column(DATETIME(fsp=6))
    is_superuser = Column(TINYINT(1), nullable=False)
    username = Column(String(150), nullable=False, unique=True)
    first_name = Column(String(150), nullable=False)
    last_name = Column(String(150), nullable=False)
    email = Column(String(254), nullable=False)
    is_staff = Column(TINYINT(1), nullable=False)
    is_active = Column(TINYINT(1), nullable=False)
    date_joined = Column(DATETIME(fsp=6), nullable=False)


class BridgeAppKey(Base):
    __tablename__ = 'bridge_app_keys'

    app_id = Column(BIGINT(20), primary_key=True)
    app_key = Column(String(60), nullable=False, server_default=text("''"))
    app_staging = Column(String(20), nullable=False, server_default=text("''"))
    app_user = Column(String(20), nullable=False)
    status = Column(INTEGER(11), nullable=False, server_default=text("1"))


class BridgeUserLogin(Base):
    __tablename__ = 'bridge_user_login'

    id = Column(INTEGER(11), primary_key=True)
    session_id = Column(Text)
    user_id = Column(BIGINT(20))
    last_seen_at = Column(DateTime)
    expired_at = Column(DateTime)
    user_agent = Column(String(50))
    status = Column(INTEGER(11))


class BridgeUserProfile(Base):
    __tablename__ = 'bridge_user_profiles'

    id = Column(INTEGER(11), primary_key=True)
    user_id = Column(INTEGER(11))
    occupation = Column(String(50))
    company = Column(String(100))
    completion = Column(INTEGER(11))
    status = Column(INTEGER(11), nullable=False, server_default=text("0"))
    created_at = Column(DateTime, nullable=False)
    updated_at = Column(DateTime, nullable=False)


class BridgeUserSecret(Base):
    __tablename__ = 'bridge_user_secrets'

    user_id = Column(BIGINT(20), primary_key=True)
    user_key = Column(String(60), nullable=False, server_default=text("''"))
    user_secret = Column(String(60), nullable=False)
    status = Column(INTEGER(11), server_default=text("1"))
    created_at = Column(DateTime, nullable=False)
    updated_at = Column(DateTime, nullable=False)


class BridgeUserToken(Base):
    __tablename__ = 'bridge_user_token'

    user_id = Column(BIGINT(20), primary_key=True)
    user_token = Column(String(60), nullable=False)
    status = Column(INTEGER(11), server_default=text("1"))
    created_at = Column(DateTime, nullable=False)
    updated_at = Column(DateTime, nullable=False)


class DealsRedeem(Base):
    __tablename__ = 'deals_redeem'

    id = Column(BIGINT(20), primary_key=True)
    postid = Column(String(255, 'utf8_unicode_ci'), nullable=False)
    userid = Column(INTEGER(11), nullable=False)
    vouchercode = Column(String(255, 'utf8_unicode_ci'), nullable=False)
    tag = Column(String(1000, 'utf8_unicode_ci'), nullable=False)
    is_active = Column(TINYINT(1), nullable=False)
    created_at = Column(DateTime, nullable=False)
    created_by = Column(String(100, 'utf8_unicode_ci'), nullable=False)
    updated_at = Column(DateTime)
    updated_by = Column(String(100, 'utf8_unicode_ci'))


class DealsVoucher(Base):
    __tablename__ = 'deals_voucher'

    id = Column(BIGINT(20), primary_key=True)
    postid = Column(String(255), nullable=False)
    userid = Column(INTEGER(11))
    vouchercode = Column(String(255), nullable=False)
    istake = Column(TINYINT(1), nullable=False)
    is_active = Column(TINYINT(1), nullable=False)
    created_at = Column(DateTime, nullable=False)
    created_by = Column(String(100), nullable=False)
    updated_at = Column(DateTime)
    updated_by = Column(String(100))


class DjangoContentType(Base):
    __tablename__ = 'django_content_type'
    __table_args__ = (
        Index('django_content_type_app_label_model_76bd3d3b_uniq', 'app_label', 'model', unique=True),
    )

    id = Column(INTEGER(11), primary_key=True)
    app_label = Column(String(100), nullable=False)
    model = Column(String(100), nullable=False)


class DjangoMigration(Base):
    __tablename__ = 'django_migrations'

    id = Column(INTEGER(11), primary_key=True)
    app = Column(String(255), nullable=False)
    name = Column(String(255), nullable=False)
    applied = Column(DATETIME(fsp=6), nullable=False)


class DjangoSession(Base):
    __tablename__ = 'django_session'

    session_key = Column(String(40), primary_key=True)
    session_data = Column(LONGTEXT, nullable=False)
    expire_date = Column(DATETIME(fsp=6), nullable=False, index=True)


class DsBanner(Base):
    __tablename__ = 'ds_banner'

    banner_id = Column(INTEGER(11), primary_key=True)
    banner_cover_title = Column(String(100))
    banner_title = Column(String(100))
    banner_img_url = Column(String(150))
    banner_url = Column(String(150))
    banner_position = Column(String(20))
    status = Column(INTEGER(11), server_default=text("1"))
    post_date = Column(DateTime)


class DsBannerHybrid(Base):
    __tablename__ = 'ds_banner_hybrid'

    banner_id = Column(INTEGER(11), primary_key=True)
    banner_cover_title = Column(String(100))
    banner_title = Column(String(100))
    banner_img_url = Column(Text)
    banner_url = Column(Text)
    banner_position = Column(String(20))
    status = Column(INTEGER(11), server_default=text("1"))
    post_date = Column(DateTime)


class DsHour(Base):
    __tablename__ = 'ds_hour'

    id = Column(INTEGER(11), primary_key=True)
    start_at = Column(DateTime)
    expired_at = Column(DateTime)
    status = Column(INTEGER(11))


class DsIespl(Base):
    __tablename__ = 'ds_iespl'

    id = Column(INTEGER(11), primary_key=True)
    post_id = Column(INTEGER(11))
    slug = Column(String(100))
    url = Column(String(100))
    title = Column(String(200))
    subtitle = Column(Text)
    img = Column(String(350))
    author = Column(String(20))
    date = Column(DateTime)
    modified = Column(DateTime)
    post_date = Column(DateTime)


class DsLongform(Base):
    __tablename__ = 'ds_longform'

    longform_id = Column(INTEGER(11), primary_key=True)
    longform_title = Column(String(100))
    longform_type = Column(String(50))
    longform_image = Column(String(100))
    longform_author = Column(String(50))
    longform_url = Column(String(100))
    status = Column(INTEGER(11))
    post_date = Column(DateTime)


class DsRecomm(Base):
    __tablename__ = 'ds_recomm'

    recomm_id = Column(INTEGER(11), primary_key=True)
    recomm_position = Column(INTEGER(11))
    recomm_type = Column(String(50))
    recomm_keyword = Column(String(50))
    recomm_status = Column(INTEGER(11))
    recomm_url = Column(String(150))
    recomm_title = Column(String(150))
    recomm_desc = Column(Text)
    recomm_img_url = Column(String(150))
    recomm_ads_url = Column(String(150))
    recomm_ads_type = Column(String(50))
    isAuto = Column(INTEGER(11))


class DsRecommHybrid(Base):
    __tablename__ = 'ds_recomm_hybrid'

    recomm_id = Column(INTEGER(11), primary_key=True)
    recomm_position = Column(INTEGER(11))
    recomm_type = Column(String(50))
    recomm_keyword = Column(String(50))
    recomm_status = Column(INTEGER(11))
    recomm_url = Column(String(150))
    recomm_title = Column(String(150))
    recomm_desc = Column(Text)
    recomm_img_url = Column(String(150))
    recomm_ads_url = Column(String(150))
    recomm_ads_type = Column(String(50))
    isAuto = Column(INTEGER(11))


class DspatchNewsletter(Base):
    __tablename__ = 'dspatch_newsletter'

    id = Column(INTEGER(11), primary_key=True)
    title = Column(String(150))
    link = Column(String(150))


class FbhackIdea(Base):
    __tablename__ = 'fbhack_idea'

    id = Column(BIGINT(20), primary_key=True)
    team_name = Column(String(255), nullable=False)
    name = Column(String(255))
    email = Column(String(255), nullable=False)
    phone = Column(String(255))
    kota = Column(String(255))
    profile = Column(String(255))
    data = Column(String(255))
    idea = Column(LONGTEXT, nullable=False)
    team_name_1 = Column(String(255))
    team_email_1 = Column(String(255))
    team_name_2 = Column(String(255))
    team_email_2 = Column(String(255))
    is_active = Column(TINYINT(1), nullable=False)
    created_at = Column(DateTime, nullable=False)
    created_by = Column(String(100), nullable=False)
    updated_at = Column(DateTime)
    updated_by = Column(String(100))


class Finhacks2016Contact(Base):
    __tablename__ = 'finhacks2016_contact'

    id = Column(BIGINT(20), primary_key=True)
    name = Column(String(255), nullable=False)
    email = Column(String(255), nullable=False)
    subject = Column(String(255), nullable=False)
    message = Column(LONGTEXT, nullable=False)
    is_active = Column(TINYINT(1), nullable=False)
    created_at = Column(DateTime, nullable=False)
    created_by = Column(String(100), nullable=False)
    updated_at = Column(DateTime)
    updated_by = Column(String(100))


class Finhacks2016Idea(Base):
    __tablename__ = 'finhacks2016_idea'

    id = Column(BIGINT(20), primary_key=True)
    name = Column(String(255), nullable=False)
    email = Column(String(255), nullable=False)
    kota = Column(String(255), nullable=False)
    profile = Column(String(255), nullable=False)
    idea = Column(LONGTEXT, nullable=False)
    team_name_1 = Column(String(255))
    team_email_1 = Column(String(255))
    team_name_2 = Column(String(255))
    team_email_2 = Column(String(255))
    is_active = Column(TINYINT(1), nullable=False)
    created_at = Column(DateTime, nullable=False)
    created_by = Column(String(100), nullable=False)
    updated_at = Column(DateTime)
    updated_by = Column(String(100))


class FosUser(Base):
    __tablename__ = 'fos_user'

    id = Column(INTEGER(11), primary_key=True)
    username = Column(String(255), nullable=False)
    username_canonical = Column(String(255), nullable=False, unique=True)
    email = Column(String(255), nullable=False)
    email_canonical = Column(String(255), nullable=False, unique=True)
    enabled = Column(TINYINT(1), nullable=False)
    salt = Column(String(255))
    password = Column(String(255), nullable=False)
    last_login = Column(DateTime)
    locked = Column(TINYINT(1), nullable=False)
    expired = Column(TINYINT(1), nullable=False)
    expires_at = Column(DateTime)
    confirmation_token = Column(String(255))
    password_requested_at = Column(DateTime)
    roles = Column(LONGTEXT, nullable=False, comment='(DC2Type:array)')
    credentials_expired = Column(TINYINT(1), nullable=False)
    credentials_expire_at = Column(DateTime)
    token = Column(String(100))


class FoundersLibrary(Base):
    __tablename__ = 'founders_library'

    fl_id = Column(INTEGER(11), primary_key=True)
    category = Column(String(50))
    category_slug = Column(String(50))
    title = Column(String(100))
    url = Column(String(100))
    description = Column(Text)
    image = Column(String(250))
    post_date = Column(DateTime)
    update_date = Column(DateTime)


class HybridSubscriptionFeature(Base):
    __tablename__ = 'hybrid_subscription_features'

    feature_id = Column(BIGINT(20), primary_key=True)
    feature_name = Column(String(60), nullable=False)
    feature_slug = Column(String(60))
    is_active = Column(TINYINT(1), nullable=False)
    created_at = Column(DateTime, nullable=False)
    updated_at = Column(DateTime, nullable=False)


class HybridSubscriptionPlan(Base):
    __tablename__ = 'hybrid_subscription_plans'

    plan_id = Column(BIGINT(20), primary_key=True)
    plan_name = Column(String(60), nullable=False)
    plan_slug = Column(String(60))
    plan_duration = Column(String(60), nullable=False)
    validity_days = Column(INTEGER(11), nullable=False)
    price = Column(INTEGER(11), nullable=False)
    plan_details = Column(Text)
    is_active = Column(TINYINT(1), nullable=False)
    created_at = Column(DateTime, nullable=False)
    updated_at = Column(DateTime, nullable=False)


class HybridSubscriptionVoucher(Base):
    __tablename__ = 'hybrid_subscription_vouchers'

    id = Column(BIGINT(20), primary_key=True)
    code = Column(String(60), nullable=False)
    name = Column(String(60))
    slug = Column(String(60), nullable=False)
    description = Column(Text)
    uses = Column(INTEGER(11), nullable=False, server_default=text("0"))
    max_uses = Column(INTEGER(11), nullable=False)
    discount_amount = Column(INTEGER(11), nullable=False)
    is_percentage = Column(TINYINT(1), nullable=False, server_default=text("1"))
    starts_at = Column(Date)
    expires_at = Column(Date)
    status = Column(INTEGER(11), server_default=text("1"))
    created_at = Column(DateTime, nullable=False)
    updated_at = Column(DateTime, nullable=False)


class HybridUser(Base):
    __tablename__ = 'hybrid_users'

    id = Column(BIGINT(20), primary_key=True)
    user_email = Column(String(60), nullable=False, unique=True)
    user_name = Column(String(60), nullable=False)
    status = Column(TINYINT(1), nullable=False, server_default=text("1"))
    created_at = Column(DateTime, nullable=False)
    updated_at = Column(DateTime, nullable=False)


class MasterSchedulePost(Base):
    __tablename__ = 'master_schedule_post'

    id = Column(INTEGER(11), primary_key=True)
    article_id = Column(INTEGER(20))
    is_repeat = Column(INTEGER(1))
    repeat_time = Column(INTEGER(5))
    repeat_every = Column(INTEGER(5))
    repeat_until = Column(Date)
    created_at = Column(DateTime)
    created_by = Column(String(150))
    updated_at = Column(DateTime)
    updated_by = Column(String(150))
    deleted = Column(INTEGER(1), server_default=text("0"))


class MstArea(Base):
    __tablename__ = 'mst_area'

    id = Column(BIGINT(20), primary_key=True)
    kota_id = Column(BIGINT(20), index=True)
    name = Column(String(255), nullable=False)
    zipcode = Column(String(6))
    is_active = Column(TINYINT(1), nullable=False)
    created_at = Column(DateTime, nullable=False)
    created_by = Column(String(100), nullable=False)
    updated_at = Column(DateTime)
    updated_by = Column(String(100))


class MstKota(Base):
    __tablename__ = 'mst_kota'

    id = Column(BIGINT(20), primary_key=True)
    provinsi_id = Column(BIGINT(20), index=True)
    name = Column(String(255), nullable=False)
    is_active = Column(TINYINT(1), nullable=False)
    created_at = Column(DateTime, nullable=False)
    created_by = Column(String(100), nullable=False)
    updated_at = Column(DateTime)
    updated_by = Column(String(100))


class MstProvinsi(Base):
    __tablename__ = 'mst_provinsi'

    id = Column(BIGINT(20), primary_key=True)
    code = Column(String(3), nullable=False)
    name = Column(String(255), nullable=False)
    is_active = Column(TINYINT(1), nullable=False)
    created_at = Column(DateTime, nullable=False)
    created_by = Column(String(100), nullable=False)
    updated_at = Column(DateTime)
    updated_by = Column(String(100))


class OauthClient(Base):
    __tablename__ = 'oauth_client'

    id = Column(BIGINT(20), primary_key=True)
    name = Column(String(100, 'utf8_unicode_ci'), nullable=False)
    description = Column(String(255, 'utf8_unicode_ci'), nullable=False)
    secret_key = Column(String(100, 'utf8_unicode_ci'), nullable=False)
    token_expires = Column(INTEGER(11), nullable=False)
    is_active = Column(TINYINT(1), nullable=False)
    created_at = Column(DateTime, nullable=False)
    created_by = Column(String(100, 'utf8_unicode_ci'), nullable=False)
    updated_at = Column(DateTime)
    updated_by = Column(String(100, 'utf8_unicode_ci'))


class OriWpCommentmeta(Base):
    __tablename__ = 'ori_wp_commentmeta'

    meta_id = Column(BIGINT(20), primary_key=True)
    comment_id = Column(BIGINT(20), nullable=False, index=True, server_default=text("0"))
    meta_key = Column(String(255), index=True)
    meta_value = Column(LONGTEXT)


class OriWpComment(Base):
    __tablename__ = 'ori_wp_comments'
    __table_args__ = (
        Index('comment_approved_date_gmt', 'comment_approved', 'comment_date_gmt'),
    )

    comment_ID = Column(BIGINT(20), primary_key=True)
    comment_post_ID = Column(BIGINT(20), nullable=False, index=True, server_default=text("0"))
    comment_author = Column(TINYTEXT, nullable=False)
    comment_author_email = Column(String(100), nullable=False, index=True, server_default=text("''"))
    comment_author_url = Column(String(200), nullable=False, server_default=text("''"))
    comment_author_IP = Column(String(100), nullable=False, server_default=text("''"))
    comment_date = Column(DateTime, nullable=False, server_default=text("'0000-00-00 00:00:00'"))
    comment_date_gmt = Column(DateTime, nullable=False, index=True, server_default=text("'0000-00-00 00:00:00'"))
    comment_content = Column(Text, nullable=False)
    comment_karma = Column(INTEGER(11), nullable=False, server_default=text("0"))
    comment_approved = Column(String(20), nullable=False, server_default=text("'1'"))
    comment_agent = Column(String(255), nullable=False, server_default=text("''"))
    comment_type = Column(String(20), nullable=False, server_default=text("''"))
    comment_parent = Column(BIGINT(20), nullable=False, index=True, server_default=text("0"))
    user_id = Column(BIGINT(20), nullable=False, server_default=text("0"))


class OriWpPostmeta(Base):
    __tablename__ = 'ori_wp_postmeta'

    meta_id = Column(BIGINT(20), primary_key=True)
    post_id = Column(BIGINT(20), nullable=False, index=True, server_default=text("0"))
    meta_key = Column(String(255), index=True)
    meta_value = Column(LONGTEXT)


class OriWpPost(Base):
    __tablename__ = 'ori_wp_posts'
    __table_args__ = (
        Index('type_status_date', 'post_type', 'post_status', 'post_date', 'ID'),
    )

    ID = Column(BIGINT(20), primary_key=True)
    post_author = Column(BIGINT(20), nullable=False, index=True, server_default=text("0"))
    post_date = Column(DateTime, nullable=False, server_default=text("'0000-00-00 00:00:00'"))
    post_date_gmt = Column(DateTime, nullable=False, server_default=text("'0000-00-00 00:00:00'"))
    post_content = Column(LONGTEXT, nullable=False)
    post_title = Column(Text, nullable=False)
    post_excerpt = Column(Text, nullable=False)
    post_status = Column(String(20), nullable=False, server_default=text("'publish'"))
    comment_status = Column(String(20), nullable=False, server_default=text("'open'"))
    ping_status = Column(String(20), nullable=False, server_default=text("'open'"))
    post_password = Column(String(20), nullable=False, server_default=text("''"))
    post_name = Column(String(200), nullable=False, index=True, server_default=text("''"))
    to_ping = Column(Text, nullable=False)
    pinged = Column(Text, nullable=False)
    post_modified = Column(DateTime, nullable=False, server_default=text("'0000-00-00 00:00:00'"))
    post_modified_gmt = Column(DateTime, nullable=False, server_default=text("'0000-00-00 00:00:00'"))
    post_content_filtered = Column(LONGTEXT, nullable=False)
    post_parent = Column(BIGINT(20), nullable=False, index=True, server_default=text("0"))
    guid = Column(String(255), nullable=False, server_default=text("''"))
    menu_order = Column(INTEGER(11), nullable=False, server_default=text("0"))
    post_type = Column(String(20), nullable=False, server_default=text("'post'"))
    post_mime_type = Column(String(100), nullable=False, server_default=text("''"))
    comment_count = Column(BIGINT(20), nullable=False, server_default=text("0"))


class OriWpUsermeta(Base):
    __tablename__ = 'ori_wp_usermeta'

    umeta_id = Column(BIGINT(20), primary_key=True)
    user_id = Column(BIGINT(20), nullable=False, index=True, server_default=text("0"))
    meta_key = Column(String(255), index=True)
    meta_value = Column(LONGTEXT)


class OriWpUser(Base):
    __tablename__ = 'ori_wp_users'

    ID = Column(BIGINT(20), primary_key=True)
    user_login = Column(String(60), nullable=False, index=True, server_default=text("''"))
    user_pass = Column(String(64), nullable=False, server_default=text("''"))
    user_nicename = Column(String(50), nullable=False, index=True, server_default=text("''"))
    user_email = Column(String(100), nullable=False, server_default=text("''"))
    user_url = Column(String(100), nullable=False, server_default=text("''"))
    user_registered = Column(DateTime, nullable=False, server_default=text("'0000-00-00 00:00:00'"))
    user_activation_key = Column(String(60), nullable=False, server_default=text("''"))
    user_status = Column(INTEGER(11), nullable=False, server_default=text("0"))
    display_name = Column(String(250), nullable=False, server_default=text("''"))


class PushnotificationMessage(Base):
    __tablename__ = 'pushnotification_message'

    id = Column(BIGINT(20), primary_key=True)
    title = Column(String(50, 'utf8_unicode_ci'), nullable=False)
    content = Column(String(85, 'utf8_unicode_ci'), nullable=False)
    url = Column(String(255, 'utf8_unicode_ci'), nullable=False)
    avatar = Column(String(255, 'utf8_unicode_ci'), nullable=False)
    schedule = Column(DateTime)
    is_active = Column(TINYINT(1), nullable=False)
    created_at = Column(DateTime, nullable=False)
    created_by = Column(String(100, 'utf8_unicode_ci'), nullable=False)
    updated_at = Column(DateTime)
    updated_by = Column(String(100, 'utf8_unicode_ci'))
    has_sent = Column(TINYINT(1), nullable=False)


class PushnotificationSubscriber(Base):
    __tablename__ = 'pushnotification_subscriber'

    id = Column(BIGINT(20), primary_key=True)
    code = Column(String(255, 'utf8_unicode_ci'), nullable=False)
    endpoint = Column(LONGTEXT, nullable=False)
    member = Column(String(11, 'utf8_unicode_ci'))
    last_sent = Column(DateTime)
    is_active = Column(TINYINT(1), nullable=False)
    created_at = Column(DateTime, nullable=False)
    created_by = Column(String(100, 'utf8_unicode_ci'), nullable=False)
    updated_at = Column(DateTime)
    updated_by = Column(String(100, 'utf8_unicode_ci'))


class ResearchDownloadCooperation(Base):
    __tablename__ = 'research_download_cooperations'

    id = Column(BIGINT(20), primary_key=True)
    post_id = Column(BIGINT(20), nullable=False)
    user_id = Column(BIGINT(20), nullable=False)
    is_checked = Column(TINYINT(1), nullable=False)
    created_at = Column(DateTime, nullable=False)
    updated_at = Column(DateTime, nullable=False)


class SchedulePost(Base):
    __tablename__ = 'schedule_post'

    id = Column(INTEGER(11), primary_key=True)
    master_schedule_post_id = Column(INTEGER(50))
    article_id = Column(INTEGER(11))
    article_title = Column(String(255))
    article_excerpt = Column(LONGTEXT)
    article_slug = Column(String(255))
    article_url = Column(LONGTEXT)
    article_thumbnail = Column(LONGTEXT)
    article_date = Column(DateTime)
    post_time = Column(DateTime)
    is_post = Column(INTEGER(1), server_default=text("0"))
    attach_image = Column(INTEGER(1), server_default=text("0"))
    type = Column(String(100))
    created_at = Column(TIMESTAMP)
    created_by = Column(String(125))
    updated_at = Column(TIMESTAMP)
    updated_by = Column(String(125))
    deleted = Column(INTEGER(1), server_default=text("0"))


class SgiAdmin(Base):
    __tablename__ = 'sgi_admin'

    admin_id = Column(INTEGER(11), primary_key=True)
    admin_username = Column(String(30))
    admin_password = Column(String(250))
    admin_name = Column(String(20))
    admin_level = Column(INTEGER(11))
    status = Column(INTEGER(11), server_default=text("1"))
    xxx = Column(String(50))


class SgiNewsreader(Base):
    __tablename__ = 'sgi_newsreader'

    article_id = Column(INTEGER(11), primary_key=True)
    article_title = Column(String(100))
    article_url = Column(String(150))
    article_slug = Column(String(150))
    article_excerpt = Column(Text)
    article_desc = Column(LONGTEXT)
    article_img = Column(String(500))
    article_publish = Column(DateTime)
    article_author = Column(String(20))
    article_category = Column(String(50))
    article_sub_category = Column(String(20))
    article_media = Column(String(50))
    article_media_url = Column(String(150))
    post_date = Column(DateTime)


class SgiNewsreaderDev(Base):
    __tablename__ = 'sgi_newsreader_dev'

    article_id = Column(INTEGER(11), primary_key=True)
    article_title = Column(String(100))
    article_url = Column(String(150))
    article_slug = Column(String(150))
    article_excerpt = Column(Text)
    article_desc = Column(LONGTEXT)
    article_img = Column(String(500))
    article_publish = Column(DateTime)
    article_author = Column(String(20))
    article_category = Column(String(50))
    article_sub_category = Column(String(20))
    article_media = Column(String(50))
    article_media_url = Column(String(150))
    post_date = Column(DateTime)


class SgiNewsreaderTmp(Base):
    __tablename__ = 'sgi_newsreader_tmp'

    article_id = Column(INTEGER(11), primary_key=True)
    article_title = Column(String(100))
    article_url = Column(String(150))
    article_slug = Column(String(150))
    article_excerpt = Column(Text)
    article_desc = Column(LONGTEXT)
    article_img = Column(String(500))
    article_publish = Column(DateTime)
    article_author = Column(String(20))
    article_category = Column(String(50))
    article_sub_category = Column(String(20))
    article_media = Column(String(50))
    article_media_url = Column(String(150))
    post_date = Column(DateTime)


class SgiPin(Base):
    __tablename__ = 'sgi_pin'

    pin_id = Column(INTEGER(11), primary_key=True)
    article_id = Column(INTEGER(11))
    channel = Column(String(20))


class SsDailysocial(Base):
    __tablename__ = 'ss_dailysocial'

    ss_id = Column(INTEGER(11), primary_key=True)
    ss_category = Column(String(50))
    ss_url = Column(String(150))
    ss_isactive = Column(INTEGER(11), server_default=text("0"))
    post_date = Column(DateTime)


class SsHybrid(Base):
    __tablename__ = 'ss_hybrid'

    ss_id = Column(INTEGER(11), primary_key=True)
    ss_category = Column(String(50))
    ss_url = Column(String(150))
    ss_isactive = Column(INTEGER(11))
    post_date = Column(DateTime)


class SubscriptionFeature(Base):
    __tablename__ = 'subscription_features'

    feature_id = Column(BIGINT(20), primary_key=True)
    feature_name = Column(String(60), nullable=False)
    feature_slug = Column(String(60))
    is_active = Column(TINYINT(1), nullable=False)
    created_at = Column(DateTime, nullable=False)
    updated_at = Column(DateTime, nullable=False)


class SubscriptionLogArticle(Base):
    __tablename__ = 'subscription_log_articles'

    id = Column(BIGINT(20), primary_key=True)
    post_id = Column(BIGINT(20), nullable=False)
    user_id = Column(BIGINT(20), nullable=False)
    post_title = Column(Text, nullable=False)
    post_slug = Column(Text, nullable=False)
    post_category = Column(String(50), nullable=False)
    post_tag = Column(String(255))
    post_author_name = Column(String(50), nullable=False)
    type = Column(String(20), nullable=False)
    created_at = Column(DateTime, nullable=False)
    updated_at = Column(DateTime, nullable=False)


class SubscriptionPlan(Base):
    __tablename__ = 'subscription_plans'

    plan_id = Column(BIGINT(20), primary_key=True)
    plan_name = Column(String(60), nullable=False)
    plan_slug = Column(String(60))
    plan_duration = Column(String(60), nullable=False, server_default=text("''"))
    validity_days = Column(INTEGER(11), nullable=False)
    price = Column(INTEGER(11), nullable=False)
    plan_details = Column(Text)
    is_active = Column(TINYINT(1), nullable=False)
    created_at = Column(DateTime, nullable=False)
    updated_at = Column(DateTime, nullable=False)


class SubscriptionVoucher(Base):
    __tablename__ = 'subscription_vouchers'

    id = Column(BIGINT(20), primary_key=True)
    code = Column(String(60), nullable=False)
    name = Column(String(60))
    slug = Column(String(60), nullable=False)
    description = Column(Text)
    uses = Column(INTEGER(11), nullable=False, server_default=text("0"))
    max_uses = Column(INTEGER(11), nullable=False)
    discount_amount = Column(INTEGER(11), nullable=False)
    is_percentage = Column(TINYINT(1), nullable=False, server_default=text("1"))
    starts_at = Column(Date)
    expires_at = Column(Date)
    status = Column(INTEGER(11), server_default=text("1"))
    created_at = Column(DateTime, nullable=False)
    updated_at = Column(DateTime, nullable=False)


class TableModify(Base):
    __tablename__ = 'table_modify'

    id = Column(BIGINT(20), primary_key=True)
    container = Column(String(100), nullable=False)
    container_id = Column(String(100), nullable=False)
    updated_value = Column(LONGTEXT, nullable=False)
    is_active = Column(TINYINT(1), nullable=False)
    created_at = Column(DateTime, nullable=False)
    created_by = Column(String(100), nullable=False)
    updated_at = Column(DateTime)
    updated_by = Column(String(100))


class TrikinetCover(Base):
    __tablename__ = 'trikinet_cover'

    cover_id = Column(INTEGER(11), primary_key=True)
    cover_title = Column(String(100))
    cover_img = Column(String(200))
    cover_tag = Column(String(50))
    status = Column(INTEGER(11))
    post_date = Column(DateTime)


class UserDownload(Base):
    __tablename__ = 'user_download'

    id = Column(BIGINT(11), primary_key=True)
    user_id = Column(INTEGER(11), nullable=False)
    post_id = Column(INTEGER(11), nullable=False)
    is_active = Column(TINYINT(1), nullable=False)
    created_at = Column(DateTime, nullable=False)
    created_by = Column(String(100), nullable=False)
    updated_at = Column(DateTime)
    updated_by = Column(String(100))
    info = Column(LONGTEXT)


class UserInbox(Base):
    __tablename__ = 'user_inbox'

    id = Column(BIGINT(20), primary_key=True)
    userid = Column(INTEGER(11))
    subject = Column(String(100), nullable=False)
    message = Column(Text, nullable=False)
    inboxfrom = Column(String(200), nullable=False)
    is_read = Column(TINYINT(1), nullable=False)
    is_active = Column(TINYINT(1), nullable=False)
    created_at = Column(DateTime, nullable=False)
    created_by = Column(String(100), nullable=False)
    updated_at = Column(DateTime)
    updated_by = Column(String(100))


class WpWPSEO404Link(Base):
    __tablename__ = 'wp_WP_SEO_404_links'

    ID = Column(INTEGER(11), primary_key=True)
    ctime = Column(DateTime, nullable=False)
    link = Column(VARCHAR(255), nullable=False, unique=True)
    referrer = Column(VARCHAR(255), nullable=False)
    ip = Column(VARCHAR(20), nullable=False)
    country = Column(VARCHAR(100), nullable=False)
    os = Column(VARCHAR(20), nullable=False)
    browser = Column(VARCHAR(20), nullable=False)


class WpWPSEOCache(Base):
    __tablename__ = 'wp_WP_SEO_Cache'

    ID = Column(INTEGER(11), primary_key=True)
    is_redirected = Column(INTEGER(1), nullable=False)
    redirect_from = Column(VARCHAR(255), nullable=False)
    redirect_to = Column(VARCHAR(255), nullable=False)
    redirect_type = Column(INTEGER(3), nullable=False, server_default=text("301"))


class WpWPSEORedirection(Base):
    __tablename__ = 'wp_WP_SEO_Redirection'

    ID = Column(INTEGER(11), primary_key=True)
    enabled = Column(INTEGER(1), nullable=False, server_default=text("1"))
    redirect_from = Column(VARCHAR(255), nullable=False, unique=True)
    redirect_from_type = Column(VARCHAR(255), nullable=False)
    redirect_from_folder_settings = Column(INTEGER(1), nullable=False)
    redirect_from_subfolders = Column(INTEGER(1), nullable=False, server_default=text("1"))
    redirect_to = Column(VARCHAR(255), nullable=False)
    redirect_to_type = Column(VARCHAR(255), nullable=False)
    redirect_to_folder_settings = Column(INTEGER(1), nullable=False, server_default=text("1"))
    regex = Column(VARCHAR(255), nullable=False)
    redirect_type = Column(VARCHAR(255), nullable=False)
    url_type = Column(INTEGER(2), nullable=False, server_default=text("1"))
    postID = Column(INTEGER(11))
    import_flag = Column(TINYINT(1), nullable=False, server_default=text("0"))
    hits = Column(INTEGER(11), nullable=False, server_default=text("0"))
    access_date = Column(DateTime)


class WpWPSEORedirectionLOG(Base):
    __tablename__ = 'wp_WP_SEO_Redirection_LOG'

    ID = Column(INTEGER(11), primary_key=True)
    rID = Column(INTEGER(11))
    postID = Column(INTEGER(11))
    ctime = Column(DateTime, nullable=False)
    rfrom = Column(VARCHAR(255), nullable=False)
    rto = Column(VARCHAR(255), nullable=False)
    rtype = Column(VARCHAR(255), nullable=False)
    rsrc = Column(VARCHAR(20), nullable=False)
    referrer = Column(VARCHAR(255), nullable=False)
    ip = Column(VARCHAR(20), nullable=False)
    country = Column(VARCHAR(100), nullable=False)
    os = Column(VARCHAR(20), nullable=False)
    browser = Column(VARCHAR(20), nullable=False)


class WpActionschedulerAction(Base):
    __tablename__ = 'wp_actionscheduler_actions'

    action_id = Column(BIGINT(20), primary_key=True)
    hook = Column(String(191, 'utf8mb4_unicode_ci'), nullable=False, index=True)
    status = Column(String(20, 'utf8mb4_unicode_ci'), nullable=False, index=True)
    scheduled_date_gmt = Column(DateTime, nullable=False, index=True, server_default=text("'0000-00-00 00:00:00'"))
    scheduled_date_local = Column(DateTime, nullable=False, server_default=text("'0000-00-00 00:00:00'"))
    args = Column(String(191, 'utf8mb4_unicode_ci'), index=True)
    schedule = Column(LONGTEXT)
    group_id = Column(BIGINT(20), nullable=False, index=True, server_default=text("0"))
    attempts = Column(INTEGER(11), nullable=False, server_default=text("0"))
    last_attempt_gmt = Column(DateTime, nullable=False, index=True, server_default=text("'0000-00-00 00:00:00'"))
    last_attempt_local = Column(DateTime, nullable=False, server_default=text("'0000-00-00 00:00:00'"))
    claim_id = Column(BIGINT(20), nullable=False, index=True, server_default=text("0"))
    extended_args = Column(String(8000, 'utf8mb4_unicode_ci'))


class WpActionschedulerClaim(Base):
    __tablename__ = 'wp_actionscheduler_claims'

    claim_id = Column(BIGINT(20), primary_key=True)
    date_created_gmt = Column(DateTime, nullable=False, index=True, server_default=text("'0000-00-00 00:00:00'"))


class WpActionschedulerGroup(Base):
    __tablename__ = 'wp_actionscheduler_groups'

    group_id = Column(BIGINT(20), primary_key=True)
    slug = Column(String(255, 'utf8mb4_unicode_ci'), nullable=False, index=True)


class WpActionschedulerLog(Base):
    __tablename__ = 'wp_actionscheduler_logs'

    log_id = Column(BIGINT(20), primary_key=True)
    action_id = Column(BIGINT(20), nullable=False, index=True)
    message = Column(Text(collation='utf8mb4_unicode_ci'), nullable=False)
    log_date_gmt = Column(DateTime, nullable=False, index=True, server_default=text("'0000-00-00 00:00:00'"))
    log_date_local = Column(DateTime, nullable=False, server_default=text("'0000-00-00 00:00:00'"))


class WpBvActivitiesStore(Base):
    __tablename__ = 'wp_bv_activities_store'

    id = Column(BIGINT(20), primary_key=True)
    site_id = Column(INTEGER(11), nullable=False)
    user_id = Column(INTEGER(11), server_default=text("0"))
    username = Column(Text(collation='utf8mb4_unicode_ci'))
    request_id = Column(Text(collation='utf8mb4_unicode_ci'))
    ip = Column(String(20, 'utf8mb4_unicode_ci'), server_default=text("''"))
    event_type = Column(String(40, 'utf8mb4_unicode_ci'), nullable=False, server_default=text("''"))
    event_data = Column(MEDIUMTEXT, nullable=False)
    time = Column(INTEGER(11))


class WpCfFormEntry(Base):
    __tablename__ = 'wp_cf_form_entries'

    id = Column(INTEGER(11), primary_key=True)
    form_id = Column(String(18), nullable=False, index=True, server_default=text("''"))
    user_id = Column(INTEGER(11), nullable=False, index=True)
    datestamp = Column(TIMESTAMP, nullable=False, index=True, server_default=text("current_timestamp()"))
    status = Column(String(20), nullable=False, index=True, server_default=text("'active'"))


class WpCfFormEntryMeta(Base):
    __tablename__ = 'wp_cf_form_entry_meta'

    meta_id = Column(BIGINT(20), primary_key=True)
    entry_id = Column(BIGINT(20), nullable=False, index=True, server_default=text("0"))
    process_id = Column(String(255))
    meta_key = Column(String(255), index=True)
    meta_value = Column(LONGTEXT)


class WpCfFormEntryValue(Base):
    __tablename__ = 'wp_cf_form_entry_values'

    id = Column(INTEGER(11), primary_key=True)
    entry_id = Column(INTEGER(11), nullable=False, index=True)
    field_id = Column(String(20), nullable=False, index=True)
    slug = Column(String(255), nullable=False, index=True, server_default=text("''"))
    value = Column(LONGTEXT, nullable=False)


class WpCommentmeta(Base):
    __tablename__ = 'wp_commentmeta'
    __table_args__ = (
        Index('disqus_dupecheck', 'meta_key', 'meta_value'),
    )

    meta_id = Column(BIGINT(20), primary_key=True)
    comment_id = Column(BIGINT(20), nullable=False, index=True, server_default=text("0"))
    meta_key = Column(String(255), index=True)
    meta_value = Column(LONGTEXT)


class WpComment(Base):
    __tablename__ = 'wp_comments'
    __table_args__ = (
        Index('comment_approved_date_gmt', 'comment_approved', 'comment_date_gmt'),
    )

    comment_ID = Column(BIGINT(20), primary_key=True)
    comment_post_ID = Column(BIGINT(20), nullable=False, index=True, server_default=text("0"))
    comment_author = Column(TINYTEXT, nullable=False)
    comment_author_email = Column(String(100), nullable=False, index=True, server_default=text("''"))
    comment_author_url = Column(String(200), nullable=False, server_default=text("''"))
    comment_author_IP = Column(String(100), nullable=False, server_default=text("''"))
    comment_date = Column(DateTime, nullable=False, server_default=text("'0000-00-00 00:00:00'"))
    comment_date_gmt = Column(DateTime, nullable=False, index=True, server_default=text("'0000-00-00 00:00:00'"))
    comment_content = Column(Text, nullable=False)
    comment_karma = Column(INTEGER(11), nullable=False, server_default=text("0"))
    comment_approved = Column(String(20), nullable=False, server_default=text("'1'"))
    comment_agent = Column(String(255), nullable=False, server_default=text("''"))
    comment_type = Column(String(20), nullable=False, server_default=text("'comment'"))
    comment_parent = Column(BIGINT(20), nullable=False, index=True, server_default=text("0"))
    user_id = Column(BIGINT(20), nullable=False, server_default=text("0"))


class WpEbdItem(Base):
    __tablename__ = 'wp_ebd_item'

    id = Column(INTEGER(11), primary_key=True)
    download_id = Column(String(128))
    file = Column(String(255))
    title = Column(VARCHAR(255))
    timestamp = Column(TIMESTAMP, nullable=False, server_default=text("current_timestamp() ON UPDATE current_timestamp()"))


t_wp_ebd_link = Table(
    'wp_ebd_link', metadata,
    Column('id', MEDIUMINT(9), nullable=False, unique=True),
    Column('item_id', INTEGER(11), nullable=False),
    Column('is_downloaded', SMALLINT(3), nullable=False, server_default=text("0")),
    Column('email', String(128), nullable=False),
    Column('expire_time', BIGINT(11)),
    Column('time_requested', BIGINT(11)),
    Column('uid', String(255), nullable=False),
    Column('selected_id', BIGINT(20), nullable=False),
    Column('delivered_as', String(255)),
    Column('is_masked', String(4)),
    Column('is_force_download', String(4))
)


t_wp_ebd_posted_data = Table(
    'wp_ebd_posted_data', metadata,
    Column('time_requested', BIGINT(20), unique=True),
    Column('email', String(128)),
    Column('user_name', VARCHAR(128)),
    Column('posted_data', Text, nullable=False)
)


class WpFormmaker(Base):
    __tablename__ = 'wp_formmaker'

    id = Column(INTEGER(11), primary_key=True)
    title = Column(String(127), nullable=False)
    mail = Column(String(128), nullable=False)
    form_front = Column(LONGTEXT, nullable=False)
    theme = Column(INTEGER(11), nullable=False)
    javascript = Column(Text, nullable=False)
    submit_text = Column(LONGTEXT, nullable=False)
    url = Column(String(200), nullable=False)
    submit_text_type = Column(TINYINT(4), nullable=False)
    script_mail = Column(Text, nullable=False)
    script_mail_user = Column(Text, nullable=False)
    counter = Column(INTEGER(11), nullable=False)
    published = Column(INTEGER(11), nullable=False, server_default=text("1"))
    label_order = Column(Text, nullable=False)
    label_order_current = Column(Text, nullable=False)
    article_id = Column(String(500), nullable=False)
    pagination = Column(String(128), nullable=False)
    show_title = Column(String(128), nullable=False)
    show_numbers = Column(String(128), nullable=False)
    public_key = Column(String(50), nullable=False)
    private_key = Column(String(50), nullable=False)
    recaptcha_theme = Column(String(20), nullable=False)
    paypal_mode = Column(INTEGER(2), nullable=False)
    checkout_mode = Column(String(20), nullable=False)
    paypal_email = Column(String(50), nullable=False)
    payment_currency = Column(String(20), nullable=False)
    tax = Column(Float, nullable=False)
    form_fields = Column(LONGTEXT, nullable=False)
    savedb = Column(TINYINT(4), nullable=False, server_default=text("1"))
    sendemail = Column(TINYINT(4), nullable=False, server_default=text("1"))
    requiredmark = Column(String(20), nullable=False, server_default=text("'*'"))
    from_mail = Column(String(128), nullable=False)
    from_name = Column(String(128), nullable=False)
    reply_to = Column(String(128), nullable=False)
    send_to = Column(String(128), nullable=False)
    autogen_layout = Column(TINYINT(4), nullable=False, server_default=text("1"))
    custom_front = Column(LONGTEXT, nullable=False)
    mail_from_user = Column(String(128), nullable=False)
    mail_from_name_user = Column(String(128), nullable=False)
    reply_to_user = Column(String(128), nullable=False)
    condition = Column(Text, nullable=False)
    mail_cc = Column(String(128), nullable=False)
    mail_cc_user = Column(String(128), nullable=False)
    mail_bcc = Column(String(128), nullable=False)
    mail_bcc_user = Column(String(128), nullable=False)
    mail_subject = Column(String(128), nullable=False)
    mail_subject_user = Column(String(128), nullable=False)
    mail_mode = Column(TINYINT(4), nullable=False, server_default=text("1"))
    mail_mode_user = Column(TINYINT(4), nullable=False, server_default=text("1"))
    mail_attachment = Column(TINYINT(4), nullable=False, server_default=text("1"))
    mail_attachment_user = Column(TINYINT(4), nullable=False, server_default=text("1"))
    user_id_wd = Column(String(220), nullable=False)
    sortable = Column(INTEGER(11), nullable=False)
    frontend_submit_fields = Column(Text, nullable=False)
    frontend_submit_stat_fields = Column(Text, nullable=False)
    mail_emptyfields = Column(TINYINT(4), nullable=False, server_default=text("0"))
    mail_verify = Column(TINYINT(4), nullable=False, server_default=text("0"))
    mail_verify_expiretime = Column(Float, nullable=False)
    mail_verification_post_id = Column(INTEGER(11), nullable=False)
    save_uploads = Column(TINYINT(4), nullable=False, server_default=text("1"))


class WpFormmakerBackup(Base):
    __tablename__ = 'wp_formmaker_backup'

    backup_id = Column(INTEGER(11), primary_key=True)
    cur = Column(INTEGER(1), nullable=False)
    id = Column(INTEGER(11), nullable=False)
    title = Column(String(127), nullable=False)
    mail = Column(String(128), nullable=False)
    form_front = Column(LONGTEXT, nullable=False)
    theme = Column(INTEGER(11), nullable=False)
    javascript = Column(Text, nullable=False)
    submit_text = Column(LONGTEXT, nullable=False)
    url = Column(String(200), nullable=False)
    submit_text_type = Column(TINYINT(4), nullable=False)
    script_mail = Column(Text, nullable=False)
    script_mail_user = Column(Text, nullable=False)
    counter = Column(INTEGER(11), nullable=False)
    published = Column(INTEGER(11), nullable=False, server_default=text("1"))
    label_order = Column(Text, nullable=False)
    label_order_current = Column(Text, nullable=False)
    article_id = Column(String(500), nullable=False)
    pagination = Column(String(128), nullable=False)
    show_title = Column(String(128), nullable=False)
    show_numbers = Column(String(128), nullable=False)
    public_key = Column(String(50), nullable=False)
    private_key = Column(String(50), nullable=False)
    recaptcha_theme = Column(String(20), nullable=False)
    paypal_mode = Column(INTEGER(2), nullable=False)
    checkout_mode = Column(String(20), nullable=False)
    paypal_email = Column(String(50), nullable=False)
    payment_currency = Column(String(20), nullable=False)
    tax = Column(Float, nullable=False)
    form_fields = Column(LONGTEXT, nullable=False)
    savedb = Column(TINYINT(4), nullable=False, server_default=text("1"))
    sendemail = Column(TINYINT(4), nullable=False, server_default=text("1"))
    requiredmark = Column(String(20), nullable=False, server_default=text("'*'"))
    from_mail = Column(String(128), nullable=False)
    from_name = Column(String(128), nullable=False)
    reply_to = Column(String(128), nullable=False)
    send_to = Column(String(128), nullable=False)
    autogen_layout = Column(TINYINT(4), nullable=False, server_default=text("1"))
    custom_front = Column(LONGTEXT, nullable=False)
    mail_from_user = Column(String(128), nullable=False)
    mail_from_name_user = Column(String(128), nullable=False)
    reply_to_user = Column(String(128), nullable=False)
    condition = Column(Text, nullable=False)
    mail_cc = Column(String(128), nullable=False)
    mail_cc_user = Column(String(128), nullable=False)
    mail_bcc = Column(String(128), nullable=False)
    mail_bcc_user = Column(String(128), nullable=False)
    mail_subject = Column(String(128), nullable=False)
    mail_subject_user = Column(String(128), nullable=False)
    mail_mode = Column(TINYINT(4), nullable=False, server_default=text("1"))
    mail_mode_user = Column(TINYINT(4), nullable=False, server_default=text("1"))
    mail_attachment = Column(TINYINT(4), nullable=False, server_default=text("1"))
    mail_attachment_user = Column(TINYINT(4), nullable=False, server_default=text("1"))
    user_id_wd = Column(String(220), nullable=False)
    sortable = Column(INTEGER(11), nullable=False)
    frontend_submit_fields = Column(Text, nullable=False)
    frontend_submit_stat_fields = Column(Text, nullable=False)
    mail_emptyfields = Column(TINYINT(4), nullable=False, server_default=text("0"))
    mail_verify = Column(TINYINT(4), nullable=False, server_default=text("0"))
    mail_verify_expiretime = Column(Float, nullable=False)
    mail_verification_post_id = Column(INTEGER(11), nullable=False)
    save_uploads = Column(TINYINT(4), nullable=False, server_default=text("1"))


class WpFormmakerBlocked(Base):
    __tablename__ = 'wp_formmaker_blocked'

    id = Column(INTEGER(11), primary_key=True)
    ip = Column(String(128), nullable=False)


class WpFormmakerQuery(Base):
    __tablename__ = 'wp_formmaker_query'

    id = Column(INTEGER(11), primary_key=True)
    form_id = Column(INTEGER(11), nullable=False)
    query = Column(Text, nullable=False)
    details = Column(Text, nullable=False)


class WpFormmakerSession(Base):
    __tablename__ = 'wp_formmaker_sessions'

    id = Column(INTEGER(11), primary_key=True)
    form_id = Column(INTEGER(20), nullable=False)
    group_id = Column(INTEGER(20), nullable=False)
    ip = Column(String(20), nullable=False)
    ord_date = Column(DateTime, nullable=False)
    ord_last_modified = Column(DateTime, nullable=False)
    status = Column(String(50), nullable=False)
    full_name = Column(String(100), nullable=False)
    email = Column(String(50), nullable=False)
    phone = Column(String(50), nullable=False)
    mobile_phone = Column(String(255), nullable=False)
    fax = Column(String(255), nullable=False)
    address = Column(String(300), nullable=False)
    paypal_info = Column(Text, nullable=False)
    without_paypal_info = Column(Text, nullable=False)
    ipn = Column(String(20), nullable=False)
    checkout_method = Column(String(20), nullable=False)
    tax = Column(Float, nullable=False)
    shipping = Column(Float, nullable=False)
    shipping_type = Column(String(200), nullable=False)
    read = Column(INTEGER(11), nullable=False)
    total = Column(Float, nullable=False)
    currency = Column(String(24), nullable=False)


class WpFormmakerSubmit(Base):
    __tablename__ = 'wp_formmaker_submits'

    id = Column(INTEGER(11), primary_key=True)
    form_id = Column(INTEGER(11), nullable=False)
    element_label = Column(String(128), nullable=False)
    element_value = Column(String(600), nullable=False)
    group_id = Column(INTEGER(11), nullable=False)
    date = Column(DateTime, nullable=False)
    ip = Column(String(32), nullable=False)
    user_id_wd = Column(INTEGER(11), nullable=False)


class WpFormmakerTheme(Base):
    __tablename__ = 'wp_formmaker_themes'

    id = Column(INTEGER(11), primary_key=True)
    title = Column(String(200), nullable=False)
    css = Column(Text, nullable=False)
    default = Column(TINYINT(4), nullable=False)


class WpFormmakerView(Base):
    __tablename__ = 'wp_formmaker_views'

    form_id = Column(INTEGER(11), primary_key=True)
    views = Column(INTEGER(50), nullable=False)


class WpHugeItContactContact(Base):
    __tablename__ = 'wp_huge_it_contact_contacts'

    id = Column(INTEGER(11), primary_key=True, unique=True)
    name = Column(String(200), nullable=False)
    hc_acceptms = Column(Text)
    hc_width = Column(INTEGER(11))
    hc_userms = Column(Text)
    hc_yourstyle = Column(Text)
    description = Column(Text)
    param = Column(Text)
    ordering = Column(INTEGER(11), nullable=False)
    published = Column(Text)


class WpHugeItContactContactsField(Base):
    __tablename__ = 'wp_huge_it_contact_contacts_fields'

    id = Column(INTEGER(11), primary_key=True, unique=True)
    name = Column(Text)
    hugeit_contact_id = Column(String(200))
    description = Column(Text)
    conttype = Column(Text, nullable=False)
    hc_field_label = Column(Text)
    hc_other_field = Column(String(128))
    field_type = Column(Text, nullable=False)
    hc_required = Column(Text, nullable=False)
    ordering = Column(INTEGER(11), nullable=False)
    published = Column(TINYINT(4))
    hc_input_show_default = Column(Text, nullable=False)
    hc_left_right = Column(Text, nullable=False)


class WpHugeItContactGeneralOption(Base):
    __tablename__ = 'wp_huge_it_contact_general_options'

    id = Column(INTEGER(11), primary_key=True)
    name = Column(String(50), nullable=False)
    title = Column(String(200), nullable=False)
    description = Column(Text, nullable=False)
    value = Column(Text, nullable=False)


class WpHugeItContactStyleField(Base):
    __tablename__ = 'wp_huge_it_contact_style_fields'

    id = Column(INTEGER(11), primary_key=True)
    name = Column(String(50), nullable=False)
    title = Column(String(200), nullable=False)
    description = Column(Text, nullable=False)
    options_name = Column(Text, nullable=False)
    value = Column(String(200), nullable=False)


class WpHugeItContactStyle(Base):
    __tablename__ = 'wp_huge_it_contact_styles'

    id = Column(INTEGER(11), primary_key=True)
    name = Column(String(50), nullable=False)
    last_update = Column(String(50), nullable=False)
    ordering = Column(INTEGER(11), nullable=False)
    published = Column(Text)


class WpHugeItContactSubmission(Base):
    __tablename__ = 'wp_huge_it_contact_submission'

    id = Column(INTEGER(11), primary_key=True)
    contact_id = Column(INTEGER(11), nullable=False)
    sub_labels = Column(Text, nullable=False)
    submission = Column(Text, nullable=False)
    submission_date = Column(Text, nullable=False)
    submission_ip = Column(Text, nullable=False)
    customer_country = Column(Text, nullable=False)
    customer_spam = Column(Text, nullable=False)
    customer_read_or_not = Column(Text, nullable=False)
    files_url = Column(Text)
    files_type = Column(Text)


class WpHugeItContactSubscriber(Base):
    __tablename__ = 'wp_huge_it_contact_subscribers'

    subscriber_id = Column(INTEGER(10), primary_key=True)
    subscriber_form_id = Column(INTEGER(10), nullable=False)
    subscriber_email = Column(String(50), nullable=False)
    text = Column(Text, nullable=False)
    send = Column(Text, nullable=False)


class WpLink(Base):
    __tablename__ = 'wp_links'

    link_id = Column(BIGINT(20), primary_key=True)
    link_url = Column(String(255), nullable=False, server_default=text("''"))
    link_name = Column(String(255), nullable=False, server_default=text("''"))
    link_image = Column(String(255), nullable=False, server_default=text("''"))
    link_target = Column(String(25), nullable=False, server_default=text("''"))
    link_description = Column(String(255), nullable=False, server_default=text("''"))
    link_visible = Column(String(20), nullable=False, index=True, server_default=text("'Y'"))
    link_owner = Column(BIGINT(20), nullable=False, server_default=text("1"))
    link_rating = Column(INTEGER(11), nullable=False, server_default=text("0"))
    link_updated = Column(DateTime, nullable=False, server_default=text("'0000-00-00 00:00:00'"))
    link_rel = Column(String(255), nullable=False, server_default=text("''"))
    link_notes = Column(MEDIUMTEXT, nullable=False)
    link_rss = Column(String(255), nullable=False, server_default=text("''"))


class WpMsSnippet(Base):
    __tablename__ = 'wp_ms_snippets'

    id = Column(BIGINT(20), primary_key=True)
    name = Column(TINYTEXT, nullable=False)
    description = Column(Text(collation='utf8mb4_unicode_ci'), nullable=False)
    code = Column(LONGTEXT, nullable=False)
    tags = Column(LONGTEXT, nullable=False)
    scope = Column(String(15, 'utf8mb4_unicode_ci'), nullable=False, server_default=text("'global'"))
    priority = Column(SMALLINT(6), nullable=False, server_default=text("10"))
    active = Column(TINYINT(1), nullable=False, server_default=text("0"))
    modified = Column(DateTime, nullable=False, server_default=text("'0000-00-00 00:00:00'"))


t_wp_nxs_log = Table(
    'wp_nxs_log', metadata,
    Column('id', BIGINT(20), nullable=False, unique=True),
    Column('date', DateTime, nullable=False, server_default=text("'0000-00-00 00:00:00'")),
    Column('act', String(255), nullable=False, server_default=text("''")),
    Column('nt', String(255), nullable=False, server_default=text("''")),
    Column('type', String(255), nullable=False, server_default=text("''")),
    Column('msg', Text, nullable=False),
    Column('extInfo', Text)
)


class WpOption(Base):
    __tablename__ = 'wp_options'

    option_id = Column(BIGINT(20), primary_key=True)
    option_name = Column(String(191), unique=True)
    option_value = Column(LONGTEXT, nullable=False)
    autoload = Column(String(20), nullable=False, index=True, server_default=text("'yes'"))


class WpPmxeExport(Base):
    __tablename__ = 'wp_pmxe_exports'

    id = Column(BIGINT(20), primary_key=True)
    parent_id = Column(BIGINT(20), nullable=False, server_default=text("0"))
    attch_id = Column(BIGINT(20), nullable=False, server_default=text("0"))
    options = Column(LONGTEXT)
    scheduled = Column(String(64, 'utf8mb4_unicode_ci'), nullable=False, server_default=text("''"))
    registered_on = Column(DateTime, nullable=False, server_default=text("'0000-00-00 00:00:00'"))
    friendly_name = Column(Text(collation='utf8mb4_unicode_ci'), nullable=False)
    exported = Column(BIGINT(20), nullable=False, server_default=text("0"))
    canceled = Column(TINYINT(1), nullable=False, server_default=text("0"))
    canceled_on = Column(DateTime, nullable=False, server_default=text("'0000-00-00 00:00:00'"))
    settings_update_on = Column(DateTime, nullable=False, server_default=text("'0000-00-00 00:00:00'"))
    last_activity = Column(DateTime, nullable=False, server_default=text("'0000-00-00 00:00:00'"))
    processing = Column(TINYINT(1), nullable=False, server_default=text("0"))
    executing = Column(TINYINT(1), nullable=False, server_default=text("0"))
    triggered = Column(TINYINT(1), nullable=False, server_default=text("0"))
    iteration = Column(BIGINT(20), nullable=False, server_default=text("0"))
    export_post_type = Column(Text(collation='utf8mb4_unicode_ci'), nullable=False)


class WpPmxeGoogleCat(Base):
    __tablename__ = 'wp_pmxe_google_cats'

    id = Column(INTEGER(11), primary_key=True)
    name = Column(String(200, 'utf8mb4_unicode_ci'), nullable=False)
    parent_id = Column(INTEGER(11), nullable=False)
    parent_name = Column(String(200, 'utf8mb4_unicode_ci'), nullable=False)
    level = Column(TINYINT(4), nullable=False)


class WpPmxePost(Base):
    __tablename__ = 'wp_pmxe_posts'

    id = Column(BIGINT(20), primary_key=True)
    post_id = Column(BIGINT(20), nullable=False)
    export_id = Column(BIGINT(20), nullable=False)
    iteration = Column(BIGINT(20), nullable=False, server_default=text("0"))


class WpPmxeTemplate(Base):
    __tablename__ = 'wp_pmxe_templates'

    id = Column(BIGINT(20), primary_key=True)
    name = Column(String(200, 'utf8mb4_unicode_ci'), nullable=False, server_default=text("''"))
    options = Column(LONGTEXT)


class WpPostmeta(Base):
    __tablename__ = 'wp_postmeta'

    meta_id = Column(BIGINT(20), primary_key=True)
    post_id = Column(BIGINT(20), nullable=False, index=True, server_default=text("0"))
    meta_key = Column(String(255), index=True)
    meta_value = Column(LONGTEXT)


class WpPost(Base):
    __tablename__ = 'wp_posts'
    __table_args__ = (
        Index('type_status_date', 'post_type', 'post_status', 'post_date', 'ID'),
        Index('wp_greet_box_post_related', 'post_title', 'post_content')
    )

    ID = Column(BIGINT(20), primary_key=True)
    post_author = Column(BIGINT(20), nullable=False, index=True, server_default=text("0"))
    post_date = Column(DateTime, nullable=False, server_default=text("'0000-00-00 00:00:00'"))
    post_date_gmt = Column(DateTime, nullable=False, server_default=text("'0000-00-00 00:00:00'"))
    post_content = Column(LONGTEXT, nullable=False, index=True)
    post_title = Column(Text, nullable=False, index=True)
    post_excerpt = Column(Text, nullable=False)
    post_status = Column(String(20), nullable=False, server_default=text("'publish'"))
    comment_status = Column(String(20), nullable=False, server_default=text("'open'"))
    ping_status = Column(String(20), nullable=False, server_default=text("'open'"))
    post_password = Column(String(255), nullable=False, server_default=text("''"))
    post_name = Column(String(200), nullable=False, index=True, server_default=text("''"))
    to_ping = Column(Text, nullable=False)
    pinged = Column(Text, nullable=False)
    post_modified = Column(DateTime, nullable=False, server_default=text("'0000-00-00 00:00:00'"))
    post_modified_gmt = Column(DateTime, nullable=False, server_default=text("'0000-00-00 00:00:00'"))
    post_content_filtered = Column(LONGTEXT, nullable=False)
    post_parent = Column(BIGINT(20), nullable=False, index=True, server_default=text("0"))
    guid = Column(String(255), nullable=False, server_default=text("''"))
    menu_order = Column(INTEGER(11), nullable=False, server_default=text("0"))
    post_type = Column(String(20), nullable=False, server_default=text("'post'"))
    post_mime_type = Column(String(100), nullable=False, server_default=text("''"))
    comment_count = Column(BIGINT(20), nullable=False, server_default=text("0"))


class WpSnippet(Base):
    __tablename__ = 'wp_snippets'

    id = Column(BIGINT(20), primary_key=True)
    name = Column(TINYTEXT, nullable=False)
    description = Column(Text(collation='utf8mb4_unicode_ci'), nullable=False)
    code = Column(LONGTEXT, nullable=False)
    tags = Column(LONGTEXT, nullable=False)
    scope = Column(String(15, 'utf8mb4_unicode_ci'), nullable=False, server_default=text("'global'"))
    priority = Column(SMALLINT(6), nullable=False, server_default=text("10"))
    active = Column(TINYINT(1), nullable=False, server_default=text("0"))
    modified = Column(DateTime, nullable=False, server_default=text("'0000-00-00 00:00:00'"))


class WpTermRelationship(Base):
    __tablename__ = 'wp_term_relationships'

    object_id = Column(BIGINT(20), primary_key=True, nullable=False, server_default=text("0"))
    term_taxonomy_id = Column(BIGINT(20), primary_key=True, nullable=False, index=True, server_default=text("0"))
    term_order = Column(INTEGER(11), nullable=False, server_default=text("0"))


class WpTermTaxonomy(Base):
    __tablename__ = 'wp_term_taxonomy'
    __table_args__ = (
        Index('term_id_taxonomy', 'term_id', 'taxonomy', unique=True),
    )

    term_taxonomy_id = Column(BIGINT(20), primary_key=True)
    term_id = Column(BIGINT(20), nullable=False, server_default=text("0"))
    taxonomy = Column(String(32), nullable=False, index=True, server_default=text("''"))
    description = Column(LONGTEXT, nullable=False)
    parent = Column(BIGINT(20), nullable=False, server_default=text("0"))
    count = Column(BIGINT(20), nullable=False, server_default=text("0"))


class WpTermmeta(Base):
    __tablename__ = 'wp_termmeta'

    meta_id = Column(BIGINT(20), primary_key=True)
    term_id = Column(BIGINT(20), nullable=False, index=True, server_default=text("0"))
    meta_key = Column(String(255, 'utf8mb4_unicode_ci'), index=True)
    meta_value = Column(LONGTEXT)


class WpTerm(Base):
    __tablename__ = 'wp_terms'

    term_id = Column(BIGINT(20), primary_key=True)
    name = Column(String(200), nullable=False, index=True, server_default=text("''"))
    slug = Column(String(200), nullable=False, index=True, server_default=text("''"))
    term_group = Column(BIGINT(10), nullable=False, server_default=text("0"))


class WpUsermeta(Base):
    __tablename__ = 'wp_usermeta'

    umeta_id = Column(BIGINT(20), primary_key=True)
    user_id = Column(BIGINT(20), ForeignKey("WpUser.ID"), nullable=False, index=True,  server_default=text("0"))
    meta_key = Column(String(255), index=True)
    meta_value = Column(LONGTEXT)


class WpUser(Base):
    __tablename__ = 'wp_users'

    ID = Column(BIGINT(20), primary_key=True)
    user_login = Column(String(60), nullable=False, index=True, server_default=text("''"))
    user_pass = Column(String(255), nullable=False, server_default=text("''"))
    user_nicename = Column(String(50), nullable=False, index=True, server_default=text("''"))
    user_email = Column(String(100), nullable=False, index=True, server_default=text("''"))
    user_url = Column(String(100), nullable=False, server_default=text("''"))
    user_registered = Column(DateTime, nullable=False, server_default=text("'0000-00-00 00:00:00'"))
    user_activation_key = Column(String(255), nullable=False, server_default=text("''"))
    user_status = Column(INTEGER(11), nullable=False, server_default=text("0"))
    display_name = Column(String(250), nullable=False, server_default=text("''"))


class WpWfblockediplog(Base):
    __tablename__ = 'wp_wfblockediplog'

    IP = Column(BINARY(16), primary_key=True, nullable=False, server_default=text("'\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0'"))
    countryCode = Column(String(2), nullable=False)
    blockCount = Column(INTEGER(10), nullable=False, server_default=text("0"))
    unixday = Column(INTEGER(10), primary_key=True, nullable=False)
    blockType = Column(String(50), primary_key=True, nullable=False, server_default=text("'generic'"))


class WpWfblocks7(Base):
    __tablename__ = 'wp_wfblocks7'

    id = Column(BIGINT(20), primary_key=True)
    type = Column(INTEGER(10), nullable=False, index=True, server_default=text("0"))
    IP = Column(BINARY(16), nullable=False, index=True, server_default=text("'\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0'"))
    blockedTime = Column(BIGINT(20), nullable=False)
    reason = Column(String(255), nullable=False)
    lastAttempt = Column(INTEGER(10), server_default=text("0"))
    blockedHits = Column(INTEGER(10), server_default=text("0"))
    expiration = Column(BIGINT(20), nullable=False, index=True, server_default=text("0"))
    parameters = Column(Text)


class WpWfconfig(Base):
    __tablename__ = 'wp_wfconfig'

    name = Column(String(100), primary_key=True)
    val = Column(LONGBLOB)
    autoload = Column(Enum('no', 'yes'), nullable=False, server_default=text("'yes'"))


class WpWfcrawler(Base):
    __tablename__ = 'wp_wfcrawlers'

    IP = Column(BINARY(16), primary_key=True, nullable=False, server_default=text("'\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0'"))
    patternSig = Column(BINARY(16), primary_key=True, nullable=False)
    status = Column(CHAR(8), nullable=False)
    lastUpdate = Column(INTEGER(10), nullable=False)
    PTR = Column(String(255), server_default=text("''"))


class WpWffilechange(Base):
    __tablename__ = 'wp_wffilechanges'

    filenameHash = Column(CHAR(64), primary_key=True)
    file = Column(String(1000), nullable=False)
    md5 = Column(CHAR(32), nullable=False)


class WpWffilemod(Base):
    __tablename__ = 'wp_wffilemods'

    filenameMD5 = Column(BINARY(16), primary_key=True)
    filename = Column(String(1000), nullable=False)
    knownFile = Column(TINYINT(3), nullable=False)
    oldMD5 = Column(BINARY(16), nullable=False)
    newMD5 = Column(BINARY(16), nullable=False)
    SHAC = Column(BINARY(32), nullable=False, server_default=text("'\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0'"))
    stoppedOnSignature = Column(String(255), nullable=False, server_default=text("''"))
    stoppedOnPosition = Column(INTEGER(10), nullable=False, server_default=text("0"))
    isSafeFile = Column(String(1), nullable=False, server_default=text("'?'"))


class WpWfhit(Base):
    __tablename__ = 'wp_wfhits'
    __table_args__ = (
        Index('k2', 'IP', 'ctime'),
    )

    id = Column(INTEGER(10), primary_key=True)
    attackLogTime = Column(Float(17, True), nullable=False, index=True)
    ctime = Column(Float(17, True), nullable=False, index=True)
    IP = Column(BINARY(16))
    jsRun = Column(TINYINT(4), server_default=text("0"))
    statusCode = Column(INTEGER(11), nullable=False, server_default=text("200"))
    isGoogle = Column(TINYINT(4), nullable=False)
    userID = Column(INTEGER(10), nullable=False)
    newVisit = Column(TINYINT(3), nullable=False)
    URL = Column(Text)
    referer = Column(Text)
    UA = Column(Text)
    action = Column(String(64), nullable=False, server_default=text("''"))
    actionDescription = Column(Text)
    actionData = Column(Text)


class WpWfhoover(Base):
    __tablename__ = 'wp_wfhoover'

    id = Column(INTEGER(10), primary_key=True)
    owner = Column(Text)
    host = Column(Text)
    path = Column(Text)
    hostKey = Column(VARBINARY(124), index=True)


class WpWfissue(Base):
    __tablename__ = 'wp_wfissues'

    id = Column(INTEGER(10), primary_key=True)
    time = Column(INTEGER(10), nullable=False)
    lastUpdated = Column(INTEGER(10), nullable=False, index=True)
    status = Column(String(10), nullable=False, index=True)
    type = Column(String(20), nullable=False)
    severity = Column(TINYINT(3), nullable=False)
    ignoreP = Column(CHAR(32), nullable=False, index=True)
    ignoreC = Column(CHAR(32), nullable=False, index=True)
    shortMsg = Column(String(255), nullable=False)
    longMsg = Column(Text)
    data = Column(Text)


class WpWfknownfilelist(Base):
    __tablename__ = 'wp_wfknownfilelist'

    id = Column(INTEGER(11), primary_key=True)
    path = Column(Text, nullable=False)


class WpWflivetraffichuman(Base):
    __tablename__ = 'wp_wflivetraffichuman'

    IP = Column(BINARY(16), primary_key=True, nullable=False, server_default=text("'\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0'"))
    identifier = Column(BINARY(32), primary_key=True, nullable=False, server_default=text("'\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0'"))
    expiration = Column(INTEGER(10), nullable=False, index=True)


class WpWfloc(Base):
    __tablename__ = 'wp_wflocs'

    IP = Column(BINARY(16), primary_key=True, server_default=text("'\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0'"))
    ctime = Column(INTEGER(10), nullable=False)
    failed = Column(TINYINT(3), nullable=False)
    city = Column(String(255), server_default=text("''"))
    region = Column(String(255), server_default=text("''"))
    countryName = Column(String(255), server_default=text("''"))
    countryCode = Column(CHAR(2), server_default=text("''"))
    lat = Column(Float(10), server_default=text("0.0000000"))
    lon = Column(Float(10), server_default=text("0.0000000"))


class WpWflogin(Base):
    __tablename__ = 'wp_wflogins'
    __table_args__ = (
        Index('k1', 'IP', 'fail'),
    )

    id = Column(INTEGER(10), primary_key=True)
    hitID = Column(INTEGER(11), index=True)
    ctime = Column(Float(17, True), nullable=False)
    fail = Column(TINYINT(3), nullable=False)
    action = Column(String(40), nullable=False)
    username = Column(String(255), nullable=False)
    userID = Column(INTEGER(10), nullable=False)
    IP = Column(BINARY(16))
    UA = Column(Text)


class WpWfls2faSecret(Base):
    __tablename__ = 'wp_wfls_2fa_secrets'

    id = Column(INTEGER(11), primary_key=True)
    user_id = Column(BIGINT(20), nullable=False, index=True)
    secret = Column(TINYBLOB, nullable=False)
    recovery = Column(LargeBinary, nullable=False)
    ctime = Column(INTEGER(10), nullable=False)
    vtime = Column(INTEGER(10), nullable=False)
    mode = Column(Enum('authenticator'), nullable=False, server_default=text("'authenticator'"))


class WpWflsSetting(Base):
    __tablename__ = 'wp_wfls_settings'

    name = Column(String(191), primary_key=True, server_default=text("''"))
    value = Column(LONGBLOB)
    autoload = Column(Enum('no', 'yes'), nullable=False, server_default=text("'yes'"))


class WpWfnotification(Base):
    __tablename__ = 'wp_wfnotifications'

    id = Column(String(32), primary_key=True, server_default=text("''"))
    new = Column(TINYINT(3), nullable=False, server_default=text("1"))
    category = Column(String(255), nullable=False)
    priority = Column(INTEGER(11), nullable=False, server_default=text("1000"))
    ctime = Column(INTEGER(10), nullable=False)
    html = Column(Text, nullable=False)
    links = Column(Text, nullable=False)


class WpWfpendingissue(Base):
    __tablename__ = 'wp_wfpendingissues'

    id = Column(INTEGER(10), primary_key=True)
    time = Column(INTEGER(10), nullable=False)
    lastUpdated = Column(INTEGER(10), nullable=False, index=True)
    status = Column(String(10), nullable=False, index=True)
    type = Column(String(20), nullable=False)
    severity = Column(TINYINT(3), nullable=False)
    ignoreP = Column(CHAR(32), nullable=False, index=True)
    ignoreC = Column(CHAR(32), nullable=False, index=True)
    shortMsg = Column(String(255), nullable=False)
    longMsg = Column(Text)
    data = Column(Text)


class WpWfreversecache(Base):
    __tablename__ = 'wp_wfreversecache'

    IP = Column(BINARY(16), primary_key=True, server_default=text("'\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0'"))
    host = Column(String(255), nullable=False)
    lastUpdate = Column(INTEGER(10), nullable=False)


class WpWfsnipcache(Base):
    __tablename__ = 'wp_wfsnipcache'

    id = Column(INTEGER(10), primary_key=True)
    IP = Column(String(45), nullable=False, index=True, server_default=text("''"))
    expiration = Column(TIMESTAMP, nullable=False, index=True, server_default=text("current_timestamp()"))
    body = Column(String(255), nullable=False, server_default=text("''"))
    count = Column(INTEGER(10), nullable=False, server_default=text("0"))
    type = Column(INTEGER(10), nullable=False, index=True, server_default=text("0"))


class WpWfstatu(Base):
    __tablename__ = 'wp_wfstatus'

    id = Column(BIGINT(20), primary_key=True)
    ctime = Column(Float(17, True), nullable=False, index=True)
    level = Column(TINYINT(3), nullable=False)
    type = Column(CHAR(5), nullable=False, index=True)
    msg = Column(String(1000), nullable=False)


class WpWftrafficrate(Base):
    __tablename__ = 'wp_wftrafficrates'

    eMin = Column(INTEGER(10), primary_key=True, nullable=False)
    IP = Column(BINARY(16), primary_key=True, nullable=False, server_default=text("'\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0'"))
    hitType = Column(Enum('hit', '404'), primary_key=True, nullable=False, server_default=text("'hit'"))
    hits = Column(INTEGER(10), nullable=False)


class WpWpmailsmtpTasksMeta(Base):
    __tablename__ = 'wp_wpmailsmtp_tasks_meta'

    id = Column(BIGINT(20), primary_key=True)
    action = Column(String(255, 'utf8mb4_unicode_ci'), nullable=False)
    data = Column(LONGTEXT, nullable=False)
    date = Column(DateTime, nullable=False)


class WpWysijaCampaign(Base):
    __tablename__ = 'wp_wysija_campaign'

    campaign_id = Column(INTEGER(10), primary_key=True)
    name = Column(String(250))
    description = Column(Text)


class WpWysijaCampaignList(Base):
    __tablename__ = 'wp_wysija_campaign_list'

    list_id = Column(INTEGER(10), primary_key=True, nullable=False)
    campaign_id = Column(INTEGER(10), primary_key=True, nullable=False)
    filter = Column(Text)


class WpWysijaCustomField(Base):
    __tablename__ = 'wp_wysija_custom_field'

    id = Column(MEDIUMINT(9), primary_key=True)
    name = Column(TINYTEXT, nullable=False)
    type = Column(TINYTEXT, nullable=False)
    required = Column(TINYINT(1), nullable=False, server_default=text("0"))
    settings = Column(Text)


class WpWysijaEmail(Base):
    __tablename__ = 'wp_wysija_email'

    email_id = Column(INTEGER(10), primary_key=True)
    campaign_id = Column(INTEGER(10), nullable=False, server_default=text("0"))
    subject = Column(String(250), nullable=False, server_default=text("''"))
    body = Column(LONGTEXT)
    created_at = Column(INTEGER(10))
    modified_at = Column(INTEGER(10))
    sent_at = Column(INTEGER(10))
    from_email = Column(String(250))
    from_name = Column(String(250))
    replyto_email = Column(String(250))
    replyto_name = Column(String(250))
    attachments = Column(Text)
    status = Column(TINYINT(4), nullable=False, server_default=text("0"))
    type = Column(TINYINT(4), nullable=False, server_default=text("1"))
    number_sent = Column(INTEGER(10), nullable=False, server_default=text("0"))
    number_opened = Column(INTEGER(10), nullable=False, server_default=text("0"))
    number_clicked = Column(INTEGER(10), nullable=False, server_default=text("0"))
    number_unsub = Column(INTEGER(10), nullable=False, server_default=text("0"))
    number_bounce = Column(INTEGER(10), nullable=False, server_default=text("0"))
    number_forward = Column(INTEGER(10), nullable=False, server_default=text("0"))
    params = Column(Text)
    wj_data = Column(LONGTEXT)
    wj_styles = Column(LONGTEXT)


class WpWysijaEmailUserStat(Base):
    __tablename__ = 'wp_wysija_email_user_stat'

    user_id = Column(INTEGER(10), primary_key=True, nullable=False)
    email_id = Column(INTEGER(10), primary_key=True, nullable=False)
    sent_at = Column(INTEGER(10), nullable=False)
    opened_at = Column(INTEGER(10))
    status = Column(TINYINT(4), nullable=False, server_default=text("0"))


class WpWysijaEmailUserUrl(Base):
    __tablename__ = 'wp_wysija_email_user_url'

    email_id = Column(INTEGER(10), primary_key=True, nullable=False)
    user_id = Column(INTEGER(10), primary_key=True, nullable=False)
    url_id = Column(INTEGER(10), primary_key=True, nullable=False)
    clicked_at = Column(INTEGER(10))
    number_clicked = Column(INTEGER(10), nullable=False, server_default=text("0"))


class WpWysijaForm(Base):
    __tablename__ = 'wp_wysija_form'

    form_id = Column(INTEGER(10), primary_key=True)
    name = Column(TINYTEXT)
    data = Column(LONGTEXT)
    styles = Column(LONGTEXT)
    subscribed = Column(INTEGER(10), nullable=False, server_default=text("0"))


class WpWysijaList(Base):
    __tablename__ = 'wp_wysija_list'

    list_id = Column(INTEGER(10), primary_key=True)
    name = Column(String(250))
    namekey = Column(String(255))
    description = Column(Text)
    unsub_mail_id = Column(INTEGER(10), nullable=False, server_default=text("0"))
    welcome_mail_id = Column(INTEGER(10), nullable=False, server_default=text("0"))
    is_enabled = Column(TINYINT(3), nullable=False, server_default=text("0"))
    is_public = Column(TINYINT(3), nullable=False, server_default=text("0"))
    created_at = Column(INTEGER(10))
    ordering = Column(INTEGER(10), nullable=False, server_default=text("0"))


class WpWysijaQueue(Base):
    __tablename__ = 'wp_wysija_queue'

    user_id = Column(INTEGER(10), primary_key=True, nullable=False)
    email_id = Column(INTEGER(10), primary_key=True, nullable=False)
    send_at = Column(INTEGER(10), nullable=False, index=True, server_default=text("0"))
    priority = Column(TINYINT(4), nullable=False, server_default=text("0"))
    number_try = Column(TINYINT(3), nullable=False, server_default=text("0"))


class WpWysijaUrl(Base):
    __tablename__ = 'wp_wysija_url'

    url_id = Column(INTEGER(10), primary_key=True)
    name = Column(String(250))
    url = Column(Text)


class WpWysijaUrlMail(Base):
    __tablename__ = 'wp_wysija_url_mail'

    email_id = Column(INTEGER(11), primary_key=True, nullable=False)
    url_id = Column(INTEGER(10), primary_key=True, nullable=False)
    unique_clicked = Column(INTEGER(10), nullable=False, server_default=text("0"))
    total_clicked = Column(INTEGER(10), nullable=False, server_default=text("0"))


class WpWysijaUser(Base):
    __tablename__ = 'wp_wysija_user'

    user_id = Column(INTEGER(10), primary_key=True)
    wpuser_id = Column(INTEGER(10), nullable=False, server_default=text("0"))
    email = Column(String(255), nullable=False, unique=True)
    firstname = Column(String(255), nullable=False, server_default=text("''"))
    lastname = Column(String(255), nullable=False, server_default=text("''"))
    ip = Column(String(100), nullable=False)
    confirmed_ip = Column(String(100), nullable=False, server_default=text("'0'"))
    confirmed_at = Column(INTEGER(10))
    last_opened = Column(INTEGER(10))
    last_clicked = Column(INTEGER(10))
    keyuser = Column(String(255), nullable=False, server_default=text("''"))
    created_at = Column(INTEGER(10))
    status = Column(TINYINT(4), nullable=False, server_default=text("0"))
    domain = Column(String(255), server_default=text("''"))


class WpWysijaUserField(Base):
    __tablename__ = 'wp_wysija_user_field'

    field_id = Column(INTEGER(10), primary_key=True)
    name = Column(String(250))
    column_name = Column(String(250), nullable=False, server_default=text("''"))
    type = Column(TINYINT(3), server_default=text("0"))
    values = Column(Text)
    default = Column(String(250), nullable=False, server_default=text("''"))
    is_required = Column(TINYINT(3), nullable=False, server_default=text("0"))
    error_message = Column(String(250), nullable=False, server_default=text("''"))


class WpWysijaUserHistory(Base):
    __tablename__ = 'wp_wysija_user_history'

    history_id = Column(INTEGER(10), primary_key=True)
    user_id = Column(INTEGER(10), nullable=False)
    email_id = Column(INTEGER(10), server_default=text("0"))
    type = Column(String(250), nullable=False, server_default=text("''"))
    details = Column(Text)
    executed_at = Column(INTEGER(10))
    executed_by = Column(INTEGER(10))
    source = Column(Text)


class WpWysijaUserList(Base):
    __tablename__ = 'wp_wysija_user_list'

    list_id = Column(INTEGER(10), primary_key=True, nullable=False)
    user_id = Column(INTEGER(10), primary_key=True, nullable=False)
    sub_date = Column(INTEGER(10), server_default=text("0"))
    unsub_date = Column(INTEGER(10), server_default=text("0"))


class WpYoastIndexable(Base):
    __tablename__ = 'wp_yoast_indexable'
    __table_args__ = (
        Index('prominent_words', 'prominent_words_version', 'object_type', 'object_sub_type', 'post_status'),
        Index('permalink_hash_and_object_type', 'permalink_hash', 'object_type'),
        Index('object_type_and_sub_type', 'object_type', 'object_sub_type'),
        Index('subpages', 'post_parent', 'object_type', 'post_status', 'object_id'),
        Index('object_id_and_type', 'object_id', 'object_type')
    )

    id = Column(INTEGER(11), primary_key=True)
    permalink = Column(LONGTEXT)
    permalink_hash = Column(String(40, 'utf8mb4_unicode_ci'))
    object_id = Column(BIGINT(20))
    object_type = Column(String(32, 'utf8mb4_unicode_ci'), nullable=False)
    object_sub_type = Column(String(32, 'utf8mb4_unicode_ci'))
    author_id = Column(BIGINT(20))
    post_parent = Column(BIGINT(20))
    title = Column(Text(collation='utf8mb4_unicode_ci'))
    description = Column(MEDIUMTEXT)
    breadcrumb_title = Column(Text(collation='utf8mb4_unicode_ci'))
    post_status = Column(String(20, 'utf8mb4_unicode_ci'))
    is_public = Column(TINYINT(1))
    is_protected = Column(TINYINT(1), server_default=text("0"))
    has_public_posts = Column(TINYINT(1))
    number_of_pages = Column(INTEGER(11))
    canonical = Column(LONGTEXT)
    primary_focus_keyword = Column(String(191, 'utf8mb4_unicode_ci'))
    primary_focus_keyword_score = Column(INTEGER(3))
    readability_score = Column(INTEGER(3))
    is_cornerstone = Column(TINYINT(1), server_default=text("0"))
    is_robots_noindex = Column(TINYINT(1), server_default=text("0"))
    is_robots_nofollow = Column(TINYINT(1), server_default=text("0"))
    is_robots_noarchive = Column(TINYINT(1), server_default=text("0"))
    is_robots_noimageindex = Column(TINYINT(1), server_default=text("0"))
    is_robots_nosnippet = Column(TINYINT(1), server_default=text("0"))
    twitter_title = Column(Text(collation='utf8mb4_unicode_ci'))
    twitter_image = Column(LONGTEXT)
    twitter_description = Column(LONGTEXT)
    twitter_image_id = Column(String(191, 'utf8mb4_unicode_ci'))
    twitter_image_source = Column(Text(collation='utf8mb4_unicode_ci'))
    open_graph_title = Column(Text(collation='utf8mb4_unicode_ci'))
    open_graph_description = Column(LONGTEXT)
    open_graph_image = Column(LONGTEXT)
    open_graph_image_id = Column(String(191, 'utf8mb4_unicode_ci'))
    open_graph_image_source = Column(Text(collation='utf8mb4_unicode_ci'))
    open_graph_image_meta = Column(MEDIUMTEXT)
    link_count = Column(INTEGER(11))
    incoming_link_count = Column(INTEGER(11))
    prominent_words_version = Column(INTEGER(11))
    created_at = Column(DateTime)
    updated_at = Column(TIMESTAMP, nullable=False, server_default=text("current_timestamp() ON UPDATE current_timestamp()"))
    blog_id = Column(BIGINT(20), nullable=False, server_default=text("1"))
    language = Column(String(32, 'utf8mb4_unicode_ci'))
    region = Column(String(32, 'utf8mb4_unicode_ci'))
    schema_page_type = Column(String(64, 'utf8mb4_unicode_ci'))
    schema_article_type = Column(String(64, 'utf8mb4_unicode_ci'))
    has_ancestors = Column(TINYINT(1), server_default=text("0"))
    estimated_reading_time_minutes = Column(INTEGER(11))


class WpYoastIndexableHierarchy(Base):
    __tablename__ = 'wp_yoast_indexable_hierarchy'

    indexable_id = Column(INTEGER(11), primary_key=True, nullable=False, index=True)
    ancestor_id = Column(INTEGER(11), primary_key=True, nullable=False, index=True)
    depth = Column(INTEGER(11), index=True)
    blog_id = Column(BIGINT(20), nullable=False, server_default=text("1"))


class WpYoastMigration(Base):
    __tablename__ = 'wp_yoast_migrations'

    id = Column(INTEGER(11), primary_key=True)
    version = Column(String(191, 'utf8mb4_unicode_ci'), unique=True)


class WpYoastPrimaryTerm(Base):
    __tablename__ = 'wp_yoast_primary_term'
    __table_args__ = (
        Index('post_taxonomy', 'post_id', 'taxonomy'),
        Index('post_term', 'post_id', 'term_id')
    )

    id = Column(INTEGER(11), primary_key=True)
    post_id = Column(BIGINT(20))
    term_id = Column(BIGINT(20))
    taxonomy = Column(String(32, 'utf8mb4_unicode_ci'), nullable=False)
    created_at = Column(DateTime)
    updated_at = Column(TIMESTAMP, nullable=False, server_default=text("current_timestamp() ON UPDATE current_timestamp()"))
    blog_id = Column(BIGINT(20), nullable=False, server_default=text("1"))


class WpYoastSeoLink(Base):
    __tablename__ = 'wp_yoast_seo_links'
    __table_args__ = (
        Index('indexable_link_direction', 'indexable_id', 'type'),
        Index('link_direction', 'post_id', 'type')
    )

    id = Column(BIGINT(20), primary_key=True)
    url = Column(String(255))
    post_id = Column(BIGINT(20))
    target_post_id = Column(BIGINT(20))
    type = Column(String(8))
    indexable_id = Column(INTEGER(11))
    target_indexable_id = Column(INTEGER(11))
    height = Column(INTEGER(11))
    width = Column(INTEGER(11))
    size = Column(INTEGER(11))
    language = Column(String(32))
    region = Column(String(32))


class AffiliateProduct(Base):
    __tablename__ = 'affiliate_product'

    id = Column(BIGINT(20), primary_key=True)
    category_id = Column(ForeignKey('affiliate_category.id'), index=True)
    title = Column(String(255, 'utf8_unicode_ci'), nullable=False)
    url = Column(VARCHAR(510), nullable=False)
    url_shortern = Column(String(255, 'utf8_unicode_ci'))
    widget = Column(LONGTEXT, nullable=False)
    article = Column(LONGTEXT, nullable=False)
    tag = Column(LONGTEXT)
    due_date = Column(DateTime)
    is_active = Column(TINYINT(1), nullable=False)
    created_at = Column(DateTime, nullable=False)
    created_by = Column(String(100, 'utf8_unicode_ci'), nullable=False)
    updated_at = Column(DateTime)
    updated_by = Column(String(100, 'utf8_unicode_ci'))

    category = relationship('AffiliateCategory')


class AuthPermission(Base):
    __tablename__ = 'auth_permission'
    __table_args__ = (
        Index('auth_permission_content_type_id_codename_01ab375a_uniq', 'content_type_id', 'codename', unique=True),
    )

    id = Column(INTEGER(11), primary_key=True)
    name = Column(String(255), nullable=False)
    content_type_id = Column(ForeignKey('django_content_type.id'), nullable=False)
    codename = Column(String(100), nullable=False)

    content_type = relationship('DjangoContentType')


class AuthUserGroup(Base):
    __tablename__ = 'auth_user_groups'
    __table_args__ = (
        Index('auth_user_groups_user_id_group_id_94350c0c_uniq', 'user_id', 'group_id', unique=True),
    )

    id = Column(INTEGER(11), primary_key=True)
    user_id = Column(ForeignKey('auth_user.id'), nullable=False)
    group_id = Column(ForeignKey('auth_group.id'), nullable=False, index=True)

    group = relationship('AuthGroup')
    user = relationship('AuthUser')


class AuthtokenToken(Base):
    __tablename__ = 'authtoken_token'

    key = Column(String(40), primary_key=True)
    created = Column(DATETIME(fsp=6), nullable=False)
    user_id = Column(ForeignKey('auth_user.id'), nullable=False, unique=True)

    user = relationship('AuthUser')


class DjangoAdminLog(Base):
    __tablename__ = 'django_admin_log'

    id = Column(INTEGER(11), primary_key=True)
    action_time = Column(DATETIME(fsp=6), nullable=False)
    object_id = Column(LONGTEXT)
    object_repr = Column(String(200), nullable=False)
    action_flag = Column(SMALLINT(5), nullable=False)
    change_message = Column(LONGTEXT, nullable=False)
    content_type_id = Column(ForeignKey('django_content_type.id'), index=True)
    user_id = Column(ForeignKey('auth_user.id'), nullable=False, index=True)

    content_type = relationship('DjangoContentType')
    user = relationship('AuthUser')


class HybridSubscriptionOrder(Base):
    __tablename__ = 'hybrid_subscription_orders'

    order_id = Column(BIGINT(20), primary_key=True)
    user_id = Column(BIGINT(20), nullable=False)
    voucher_id = Column(ForeignKey('hybrid_subscription_vouchers.id'), index=True)
    order_number = Column(Text, nullable=False)
    gross_amount = Column(INTEGER(11))
    payment_method = Column(String(60))
    payment_amount = Column(INTEGER(11))
    payment_status = Column(INTEGER(11), server_default=text("0"))
    order_details = Column(Text)
    payment_details = Column(Text)
    created_at = Column(DateTime, nullable=False)
    updated_at = Column(DateTime, nullable=False)

    voucher = relationship('HybridSubscriptionVoucher')


t_hybrid_subscription_plan_features = Table(
    'hybrid_subscription_plan_features', metadata,
    Column('is_checked', TINYINT(1), nullable=False),
    Column('feature_id', ForeignKey('hybrid_subscription_features.feature_id', ondelete='CASCADE', onupdate='CASCADE'), index=True),
    Column('plan_id', ForeignKey('hybrid_subscription_plans.plan_id', ondelete='CASCADE', onupdate='CASCADE'), index=True),
    Column('created_at', DateTime, nullable=False),
    Column('updated_at', DateTime, nullable=False)
)


class HybridSubscriptionVouchersPlan(Base):
    __tablename__ = 'hybrid_subscription_vouchers_plans'
    __table_args__ = (
        Index('hybrid_subscription_vouchers_plans_plan_id_voucher_id', 'plan_id', 'voucher_id', unique=True),
    )

    status = Column(INTEGER(11), server_default=text("1"))
    created_at = Column(DateTime, nullable=False)
    updated_at = Column(DateTime, nullable=False)
    plan_id = Column(ForeignKey('hybrid_subscription_plans.plan_id', ondelete='CASCADE', onupdate='CASCADE'), primary_key=True, nullable=False)
    voucher_id = Column(ForeignKey('hybrid_subscription_vouchers.id', ondelete='CASCADE', onupdate='CASCADE'), primary_key=True, nullable=False, index=True)

    plan = relationship('HybridSubscriptionPlan')
    voucher = relationship('HybridSubscriptionVoucher')


class HybridSubscriptionVouchersRedeem(Base):
    __tablename__ = 'hybrid_subscription_vouchers_redeems'
    __table_args__ = (
        Index('hybrid_subscription_vouchers_redeems_user_id_voucher_id', 'user_id', 'voucher_id', unique=True),
    )

    is_take = Column(INTEGER(11), server_default=text("0"))
    created_at = Column(DateTime, nullable=False)
    updated_at = Column(DateTime, nullable=False)
    user_id = Column(BIGINT(20), primary_key=True, nullable=False)
    voucher_id = Column(ForeignKey('hybrid_subscription_vouchers.id', ondelete='CASCADE', onupdate='CASCADE'), primary_key=True, nullable=False, index=True)

    voucher = relationship('HybridSubscriptionVoucher')


class OauthToken(Base):
    __tablename__ = 'oauth_token'

    id = Column(BIGINT(20), primary_key=True)
    oauth_client_id = Column(ForeignKey('oauth_client.id'), index=True)
    user_id = Column(ForeignKey('fos_user.id'), index=True)
    token = Column(String(100, 'utf8_unicode_ci'), nullable=False)
    expires = Column(DateTime, nullable=False)
    is_active = Column(TINYINT(1), nullable=False)
    created_at = Column(DateTime, nullable=False)
    created_by = Column(String(100, 'utf8_unicode_ci'), nullable=False)
    updated_at = Column(DateTime)
    updated_by = Column(String(100, 'utf8_unicode_ci'))

    oauth_client = relationship('OauthClient')
    user = relationship('FosUser')


class SubscriptionOrder(Base):
    __tablename__ = 'subscription_orders'

    order_id = Column(BIGINT(20), primary_key=True)
    user_id = Column(BIGINT(20), nullable=False)
    voucher_id = Column(ForeignKey('subscription_vouchers.id'), index=True)
    order_number = Column(Text, nullable=False)
    gross_amount = Column(INTEGER(11))
    payment_method = Column(String(60))
    payment_amount = Column(INTEGER(11))
    payment_status = Column(INTEGER(11), server_default=text("0"))
    order_details = Column(Text)
    payment_details = Column(Text)
    created_at = Column(DateTime, nullable=False)
    updated_at = Column(DateTime, nullable=False)

    voucher = relationship('SubscriptionVoucher')


class SubscriptionPlanFeature(Base):
    __tablename__ = 'subscription_plan_features'

    is_checked = Column(TINYINT(1), nullable=False)
    created_at = Column(DateTime, nullable=False)
    updated_at = Column(DateTime, nullable=False)
    feature_id = Column(ForeignKey('subscription_features.feature_id', ondelete='CASCADE', onupdate='CASCADE'), primary_key=True, nullable=False)
    plan_id = Column(ForeignKey('subscription_plans.plan_id', ondelete='CASCADE', onupdate='CASCADE'), primary_key=True, nullable=False, index=True)

    feature = relationship('SubscriptionFeature')
    plan = relationship('SubscriptionPlan')


class SubscriptionVouchersPlan(Base):
    __tablename__ = 'subscription_vouchers_plans'
    __table_args__ = (
        Index('subscription_vouchers_plans_plan_id_voucher_id', 'plan_id', 'voucher_id', unique=True),
    )

    status = Column(INTEGER(11), server_default=text("1"))
    created_at = Column(DateTime, nullable=False)
    updated_at = Column(DateTime, nullable=False)
    plan_id = Column(ForeignKey('subscription_plans.plan_id', ondelete='CASCADE', onupdate='CASCADE'), primary_key=True, nullable=False)
    voucher_id = Column(ForeignKey('subscription_vouchers.id', ondelete='CASCADE', onupdate='CASCADE'), primary_key=True, nullable=False, index=True)

    plan = relationship('SubscriptionPlan')
    voucher = relationship('SubscriptionVoucher')


class SubscriptionVouchersRedeem(Base):
    __tablename__ = 'subscription_vouchers_redeems'
    __table_args__ = (
        Index('subscription_vouchers_redeems_user_id_voucher_id', 'user_id', 'voucher_id', unique=True),
    )

    is_take = Column(INTEGER(11), server_default=text("0"))
    created_at = Column(DateTime, nullable=False)
    updated_at = Column(DateTime, nullable=False)
    user_id = Column(BIGINT(20), primary_key=True, nullable=False)
    voucher_id = Column(ForeignKey('subscription_vouchers.id', ondelete='CASCADE', onupdate='CASCADE'), primary_key=True, nullable=False, index=True)

    voucher = relationship('SubscriptionVoucher')


class AuthGroupPermission(Base):
    __tablename__ = 'auth_group_permissions'
    __table_args__ = (
        Index('auth_group_permissions_group_id_permission_id_0cd325b0_uniq', 'group_id', 'permission_id', unique=True),
    )

    id = Column(INTEGER(11), primary_key=True)
    group_id = Column(ForeignKey('auth_group.id'), nullable=False)
    permission_id = Column(ForeignKey('auth_permission.id'), nullable=False, index=True)

    group = relationship('AuthGroup')
    permission = relationship('AuthPermission')


class AuthUserUserPermission(Base):
    __tablename__ = 'auth_user_user_permissions'
    __table_args__ = (
        Index('auth_user_user_permissions_user_id_permission_id_14a6b632_uniq', 'user_id', 'permission_id', unique=True),
    )

    id = Column(INTEGER(11), primary_key=True)
    user_id = Column(ForeignKey('auth_user.id'), nullable=False)
    permission_id = Column(ForeignKey('auth_permission.id'), nullable=False, index=True)

    permission = relationship('AuthPermission')
    user = relationship('AuthUser')


class HybridSubscriptionLogEmailPayment(Base):
    __tablename__ = 'hybrid_subscription_log_email_payments'

    email_id = Column(BIGINT(20), primary_key=True)
    order_id = Column(ForeignKey('hybrid_subscription_orders.order_id', ondelete='CASCADE', onupdate='CASCADE'), index=True)
    payment_status = Column(INTEGER(11))
    created_at = Column(DateTime, nullable=False)
    updated_at = Column(DateTime, nullable=False)

    order = relationship('HybridSubscriptionOrder')


class HybridSubscription(Base):
    __tablename__ = 'hybrid_subscriptions'

    subscription_id = Column(BIGINT(20), primary_key=True)
    user_id = Column(BIGINT(20), nullable=False)
    plan_id = Column(ForeignKey('hybrid_subscription_plans.plan_id', onupdate='CASCADE'), nullable=False, index=True)
    order_id = Column(ForeignKey('hybrid_subscription_orders.order_id', ondelete='CASCADE', onupdate='CASCADE'), nullable=False, unique=True)
    is_active = Column(TINYINT(1), nullable=False)
    start_date = Column(Date, nullable=False)
    end_date = Column(Date, nullable=False)
    created_at = Column(DateTime, nullable=False)
    updated_at = Column(DateTime, nullable=False)

    order = relationship('HybridSubscriptionOrder')
    plan = relationship('HybridSubscriptionPlan')


class SubscriptionLogEmailPayment(Base):
    __tablename__ = 'subscription_log_email_payments'

    email_id = Column(BIGINT(20), primary_key=True)
    order_id = Column(ForeignKey('subscription_orders.order_id', ondelete='CASCADE', onupdate='CASCADE'), nullable=False, index=True)
    payment_status = Column(INTEGER(11))
    created_at = Column(DateTime, nullable=False)
    updated_at = Column(DateTime, nullable=False)

    order = relationship('SubscriptionOrder')


class Subscription(Base):
    __tablename__ = 'subscriptions'

    subscription_id = Column(BIGINT(20), primary_key=True)
    user_id = Column(BIGINT(20), nullable=False)
    plan_id = Column(ForeignKey('subscription_plans.plan_id', onupdate='CASCADE'), nullable=False, index=True)
    order_id = Column(ForeignKey('subscription_orders.order_id', ondelete='CASCADE', onupdate='CASCADE'), nullable=False, unique=True)
    is_active = Column(TINYINT(1), nullable=False)
    start_date = Column(DateTime, nullable=False)
    end_date = Column(DateTime, nullable=False)
    created_at = Column(DateTime, nullable=False)
    updated_at = Column(DateTime, nullable=False)

    order = relationship('SubscriptionOrder')
    plan = relationship('SubscriptionPlan')
