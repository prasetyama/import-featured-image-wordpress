# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AffiliateCategory(models.Model):
    id = models.BigAutoField(primary_key=True)
    reference = models.ForeignKey('self', models.DO_NOTHING, db_column='reference', blank=True, null=True)
    name = models.CharField(max_length=255)
    is_active = models.IntegerField()
    created_at = models.DateTimeField()
    created_by = models.CharField(max_length=100)
    updated_at = models.DateTimeField(blank=True, null=True)
    updated_by = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'affiliate_category'


class AffiliateProduct(models.Model):
    id = models.BigAutoField(primary_key=True)
    category = models.ForeignKey(AffiliateCategory, models.DO_NOTHING, blank=True, null=True)
    title = models.CharField(max_length=255)
    url = models.CharField(max_length=510, db_collation='utf8_general_ci')
    url_shortern = models.CharField(max_length=255, blank=True, null=True)
    widget = models.TextField()
    article = models.TextField()
    tag = models.TextField(blank=True, null=True)
    due_date = models.DateTimeField(blank=True, null=True)
    is_active = models.IntegerField()
    created_at = models.DateTimeField()
    created_by = models.CharField(max_length=100)
    updated_at = models.DateTimeField(blank=True, null=True)
    updated_by = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'affiliate_product'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class AuthtokenToken(models.Model):
    key = models.CharField(primary_key=True, max_length=40)
    created = models.DateTimeField()
    user = models.OneToOneField(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'authtoken_token'


class BridgeAppKeys(models.Model):
    app_id = models.BigAutoField(primary_key=True)
    app_key = models.CharField(max_length=60)
    app_staging = models.CharField(max_length=20)
    app_user = models.CharField(max_length=20)
    status = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'bridge_app_keys'


class BridgeUserLogin(models.Model):
    session_id = models.TextField(blank=True, null=True)
    user_id = models.BigIntegerField(blank=True, null=True)
    last_seen_at = models.DateTimeField(blank=True, null=True)
    expired_at = models.DateTimeField(blank=True, null=True)
    user_agent = models.CharField(max_length=50, blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'bridge_user_login'


class BridgeUserProfiles(models.Model):
    user_id = models.IntegerField(blank=True, null=True)
    occupation = models.CharField(max_length=50, blank=True, null=True)
    company = models.CharField(max_length=100, blank=True, null=True)
    completion = models.IntegerField(blank=True, null=True)
    status = models.IntegerField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'bridge_user_profiles'


class BridgeUserSecrets(models.Model):
    user_id = models.BigIntegerField(primary_key=True)
    user_key = models.CharField(max_length=60)
    user_secret = models.CharField(max_length=60)
    status = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'bridge_user_secrets'


class BridgeUserToken(models.Model):
    user_id = models.BigIntegerField(primary_key=True)
    user_token = models.CharField(max_length=60)
    status = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'bridge_user_token'


class DealsRedeem(models.Model):
    id = models.BigAutoField(primary_key=True)
    postid = models.CharField(max_length=255)
    userid = models.IntegerField()
    vouchercode = models.CharField(max_length=255)
    tag = models.CharField(max_length=1000)
    is_active = models.IntegerField()
    created_at = models.DateTimeField()
    created_by = models.CharField(max_length=100)
    updated_at = models.DateTimeField(blank=True, null=True)
    updated_by = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'deals_redeem'


class DealsVoucher(models.Model):
    id = models.BigAutoField(primary_key=True)
    postid = models.CharField(max_length=255)
    userid = models.IntegerField(blank=True, null=True)
    vouchercode = models.CharField(max_length=255)
    istake = models.IntegerField()
    is_active = models.IntegerField()
    created_at = models.DateTimeField()
    created_by = models.CharField(max_length=100)
    updated_at = models.DateTimeField(blank=True, null=True)
    updated_by = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'deals_voucher'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class DsBanner(models.Model):
    banner_id = models.AutoField(primary_key=True)
    banner_cover_title = models.CharField(max_length=100, blank=True, null=True)
    banner_title = models.CharField(max_length=100, blank=True, null=True)
    banner_img_url = models.CharField(max_length=150, blank=True, null=True)
    banner_url = models.CharField(max_length=150, blank=True, null=True)
    banner_position = models.CharField(max_length=20, blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    post_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ds_banner'


class DsBannerHybrid(models.Model):
    banner_id = models.AutoField(primary_key=True)
    banner_cover_title = models.CharField(max_length=100, blank=True, null=True)
    banner_title = models.CharField(max_length=100, blank=True, null=True)
    banner_img_url = models.TextField(blank=True, null=True)
    banner_url = models.TextField(blank=True, null=True)
    banner_position = models.CharField(max_length=20, blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    post_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ds_banner_hybrid'


class DsHour(models.Model):
    start_at = models.DateTimeField(blank=True, null=True)
    expired_at = models.DateTimeField(blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ds_hour'


class DsIespl(models.Model):
    post_id = models.IntegerField(blank=True, null=True)
    slug = models.CharField(max_length=100, blank=True, null=True)
    url = models.CharField(max_length=100, blank=True, null=True)
    title = models.CharField(max_length=200, blank=True, null=True)
    subtitle = models.TextField(blank=True, null=True)
    img = models.CharField(max_length=350, blank=True, null=True)
    author = models.CharField(max_length=20, blank=True, null=True)
    date = models.DateTimeField(blank=True, null=True)
    modified = models.DateTimeField(blank=True, null=True)
    post_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ds_iespl'


class DsLongform(models.Model):
    longform_id = models.AutoField(primary_key=True)
    longform_title = models.CharField(max_length=100, blank=True, null=True)
    longform_type = models.CharField(max_length=50, blank=True, null=True)
    longform_image = models.CharField(max_length=100, blank=True, null=True)
    longform_author = models.CharField(max_length=50, blank=True, null=True)
    longform_url = models.CharField(max_length=100, blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    post_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ds_longform'


class DsRecomm(models.Model):
    recomm_id = models.AutoField(primary_key=True)
    recomm_position = models.IntegerField(blank=True, null=True)
    recomm_type = models.CharField(max_length=50, blank=True, null=True)
    recomm_keyword = models.CharField(max_length=50, blank=True, null=True)
    recomm_status = models.IntegerField(blank=True, null=True)
    recomm_url = models.CharField(max_length=150, blank=True, null=True)
    recomm_title = models.CharField(max_length=150, blank=True, null=True)
    recomm_desc = models.TextField(blank=True, null=True)
    recomm_img_url = models.CharField(max_length=150, blank=True, null=True)
    recomm_ads_url = models.CharField(max_length=150, blank=True, null=True)
    recomm_ads_type = models.CharField(max_length=50, blank=True, null=True)
    isauto = models.IntegerField(db_column='isAuto', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ds_recomm'


class DsRecommHybrid(models.Model):
    recomm_id = models.AutoField(primary_key=True)
    recomm_position = models.IntegerField(blank=True, null=True)
    recomm_type = models.CharField(max_length=50, blank=True, null=True)
    recomm_keyword = models.CharField(max_length=50, blank=True, null=True)
    recomm_status = models.IntegerField(blank=True, null=True)
    recomm_url = models.CharField(max_length=150, blank=True, null=True)
    recomm_title = models.CharField(max_length=150, blank=True, null=True)
    recomm_desc = models.TextField(blank=True, null=True)
    recomm_img_url = models.CharField(max_length=150, blank=True, null=True)
    recomm_ads_url = models.CharField(max_length=150, blank=True, null=True)
    recomm_ads_type = models.CharField(max_length=50, blank=True, null=True)
    isauto = models.IntegerField(db_column='isAuto', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ds_recomm_hybrid'


class DspatchNewsletter(models.Model):
    title = models.CharField(max_length=150, blank=True, null=True)
    link = models.CharField(max_length=150, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dspatch_newsletter'


class FbhackIdea(models.Model):
    id = models.BigAutoField(primary_key=True)
    team_name = models.CharField(max_length=255)
    name = models.CharField(max_length=255, blank=True, null=True)
    email = models.CharField(max_length=255)
    phone = models.CharField(max_length=255, blank=True, null=True)
    kota = models.CharField(max_length=255, blank=True, null=True)
    profile = models.CharField(max_length=255, blank=True, null=True)
    data = models.CharField(max_length=255, blank=True, null=True)
    idea = models.TextField()
    team_name_1 = models.CharField(max_length=255, blank=True, null=True)
    team_email_1 = models.CharField(max_length=255, blank=True, null=True)
    team_name_2 = models.CharField(max_length=255, blank=True, null=True)
    team_email_2 = models.CharField(max_length=255, blank=True, null=True)
    is_active = models.IntegerField()
    created_at = models.DateTimeField()
    created_by = models.CharField(max_length=100)
    updated_at = models.DateTimeField(blank=True, null=True)
    updated_by = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'fbhack_idea'


class Finhacks2016Contact(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    subject = models.CharField(max_length=255)
    message = models.TextField()
    is_active = models.IntegerField()
    created_at = models.DateTimeField()
    created_by = models.CharField(max_length=100)
    updated_at = models.DateTimeField(blank=True, null=True)
    updated_by = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'finhacks2016_contact'


class Finhacks2016Idea(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    kota = models.CharField(max_length=255)
    profile = models.CharField(max_length=255)
    idea = models.TextField()
    team_name_1 = models.CharField(max_length=255, blank=True, null=True)
    team_email_1 = models.CharField(max_length=255, blank=True, null=True)
    team_name_2 = models.CharField(max_length=255, blank=True, null=True)
    team_email_2 = models.CharField(max_length=255, blank=True, null=True)
    is_active = models.IntegerField()
    created_at = models.DateTimeField()
    created_by = models.CharField(max_length=100)
    updated_at = models.DateTimeField(blank=True, null=True)
    updated_by = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'finhacks2016_idea'


class FosUser(models.Model):
    username = models.CharField(max_length=255)
    username_canonical = models.CharField(unique=True, max_length=255)
    email = models.CharField(max_length=255)
    email_canonical = models.CharField(unique=True, max_length=255)
    enabled = models.IntegerField()
    salt = models.CharField(max_length=255, blank=True, null=True)
    password = models.CharField(max_length=255)
    last_login = models.DateTimeField(blank=True, null=True)
    locked = models.IntegerField()
    expired = models.IntegerField()
    expires_at = models.DateTimeField(blank=True, null=True)
    confirmation_token = models.CharField(max_length=255, blank=True, null=True)
    password_requested_at = models.DateTimeField(blank=True, null=True)
    roles = models.TextField()
    credentials_expired = models.IntegerField()
    credentials_expire_at = models.DateTimeField(blank=True, null=True)
    token = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'fos_user'


class FoundersLibrary(models.Model):
    fl_id = models.AutoField(primary_key=True)
    category = models.CharField(max_length=50, blank=True, null=True)
    category_slug = models.CharField(max_length=50, blank=True, null=True)
    title = models.CharField(max_length=100, blank=True, null=True)
    url = models.CharField(max_length=100, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    image = models.CharField(max_length=250, blank=True, null=True)
    post_date = models.DateTimeField(blank=True, null=True)
    update_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'founders_library'


class HybridSubscriptionFeatures(models.Model):
    feature_id = models.BigAutoField(primary_key=True)
    feature_name = models.CharField(max_length=60)
    feature_slug = models.CharField(max_length=60, blank=True, null=True)
    is_active = models.IntegerField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'hybrid_subscription_features'


class HybridSubscriptionLogEmailPayments(models.Model):
    email_id = models.BigAutoField(primary_key=True)
    order = models.ForeignKey('HybridSubscriptionOrders', models.DO_NOTHING, blank=True, null=True)
    payment_status = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'hybrid_subscription_log_email_payments'


class HybridSubscriptionOrders(models.Model):
    order_id = models.BigAutoField(primary_key=True)
    user_id = models.BigIntegerField()
    voucher = models.ForeignKey('HybridSubscriptionVouchers', models.DO_NOTHING, blank=True, null=True)
    order_number = models.TextField()
    gross_amount = models.IntegerField(blank=True, null=True)
    payment_method = models.CharField(max_length=60, blank=True, null=True)
    payment_amount = models.IntegerField(blank=True, null=True)
    payment_status = models.IntegerField(blank=True, null=True)
    order_details = models.TextField(blank=True, null=True)
    payment_details = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'hybrid_subscription_orders'


class HybridSubscriptionPlanFeatures(models.Model):
    is_checked = models.IntegerField()
    feature = models.ForeignKey(HybridSubscriptionFeatures, models.DO_NOTHING, blank=True, null=True)
    plan = models.ForeignKey('HybridSubscriptionPlans', models.DO_NOTHING, blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'hybrid_subscription_plan_features'


class HybridSubscriptionPlans(models.Model):
    plan_id = models.BigAutoField(primary_key=True)
    plan_name = models.CharField(max_length=60)
    plan_slug = models.CharField(max_length=60, blank=True, null=True)
    plan_duration = models.CharField(max_length=60)
    validity_days = models.IntegerField()
    price = models.IntegerField()
    plan_details = models.TextField(blank=True, null=True)
    is_active = models.IntegerField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'hybrid_subscription_plans'


class HybridSubscriptionVouchers(models.Model):
    id = models.BigAutoField(primary_key=True)
    code = models.CharField(max_length=60)
    name = models.CharField(max_length=60, blank=True, null=True)
    slug = models.CharField(max_length=60)
    description = models.TextField(blank=True, null=True)
    uses = models.IntegerField()
    max_uses = models.IntegerField()
    discount_amount = models.IntegerField()
    is_percentage = models.IntegerField()
    starts_at = models.DateField(blank=True, null=True)
    expires_at = models.DateField(blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'hybrid_subscription_vouchers'


class HybridSubscriptionVouchersPlans(models.Model):
    status = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    plan = models.OneToOneField(HybridSubscriptionPlans, models.DO_NOTHING, primary_key=True)
    voucher = models.ForeignKey(HybridSubscriptionVouchers, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'hybrid_subscription_vouchers_plans'
        unique_together = (('plan', 'voucher'), ('plan', 'voucher'),)


class HybridSubscriptionVouchersRedeems(models.Model):
    is_take = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    user_id = models.BigIntegerField(primary_key=True)
    voucher = models.ForeignKey(HybridSubscriptionVouchers, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'hybrid_subscription_vouchers_redeems'
        unique_together = (('user_id', 'voucher'), ('user_id', 'voucher'),)


class HybridSubscriptions(models.Model):
    subscription_id = models.BigAutoField(primary_key=True)
    user_id = models.BigIntegerField()
    plan = models.ForeignKey(HybridSubscriptionPlans, models.DO_NOTHING)
    order = models.OneToOneField(HybridSubscriptionOrders, models.DO_NOTHING)
    is_active = models.IntegerField()
    start_date = models.DateField()
    end_date = models.DateField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'hybrid_subscriptions'


class HybridUsers(models.Model):
    id = models.BigAutoField(primary_key=True)
    user_email = models.CharField(unique=True, max_length=60)
    user_name = models.CharField(max_length=60)
    status = models.IntegerField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'hybrid_users'


class MasterSchedulePost(models.Model):
    article_id = models.IntegerField(blank=True, null=True)
    is_repeat = models.IntegerField(blank=True, null=True)
    repeat_time = models.IntegerField(blank=True, null=True)
    repeat_every = models.IntegerField(blank=True, null=True)
    repeat_until = models.DateField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    created_by = models.CharField(max_length=150, blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    updated_by = models.CharField(max_length=150, blank=True, null=True)
    deleted = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'master_schedule_post'


class MstArea(models.Model):
    id = models.BigAutoField(primary_key=True)
    kota_id = models.BigIntegerField(blank=True, null=True)
    name = models.CharField(max_length=255)
    zipcode = models.CharField(max_length=6, blank=True, null=True)
    is_active = models.IntegerField()
    created_at = models.DateTimeField()
    created_by = models.CharField(max_length=100)
    updated_at = models.DateTimeField(blank=True, null=True)
    updated_by = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mst_area'


class MstKota(models.Model):
    id = models.BigAutoField(primary_key=True)
    provinsi_id = models.BigIntegerField(blank=True, null=True)
    name = models.CharField(max_length=255)
    is_active = models.IntegerField()
    created_at = models.DateTimeField()
    created_by = models.CharField(max_length=100)
    updated_at = models.DateTimeField(blank=True, null=True)
    updated_by = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mst_kota'


class MstProvinsi(models.Model):
    id = models.BigAutoField(primary_key=True)
    code = models.CharField(max_length=3)
    name = models.CharField(max_length=255)
    is_active = models.IntegerField()
    created_at = models.DateTimeField()
    created_by = models.CharField(max_length=100)
    updated_at = models.DateTimeField(blank=True, null=True)
    updated_by = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mst_provinsi'


class OauthClient(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=255)
    secret_key = models.CharField(max_length=100)
    token_expires = models.IntegerField()
    is_active = models.IntegerField()
    created_at = models.DateTimeField()
    created_by = models.CharField(max_length=100)
    updated_at = models.DateTimeField(blank=True, null=True)
    updated_by = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'oauth_client'


class OauthToken(models.Model):
    id = models.BigAutoField(primary_key=True)
    oauth_client = models.ForeignKey(OauthClient, models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(FosUser, models.DO_NOTHING, blank=True, null=True)
    token = models.CharField(max_length=100)
    expires = models.DateTimeField()
    is_active = models.IntegerField()
    created_at = models.DateTimeField()
    created_by = models.CharField(max_length=100)
    updated_at = models.DateTimeField(blank=True, null=True)
    updated_by = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'oauth_token'


class OriWpCommentmeta(models.Model):
    meta_id = models.BigAutoField(primary_key=True)
    comment_id = models.PositiveBigIntegerField()
    meta_key = models.CharField(max_length=255, blank=True, null=True)
    meta_value = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ori_wp_commentmeta'


class OriWpComments(models.Model):
    comment_id = models.BigAutoField(db_column='comment_ID', primary_key=True)  # Field name made lowercase.
    comment_post_id = models.PositiveBigIntegerField(db_column='comment_post_ID')  # Field name made lowercase.
    comment_author = models.TextField()
    comment_author_email = models.CharField(max_length=100)
    comment_author_url = models.CharField(max_length=200)
    comment_author_ip = models.CharField(db_column='comment_author_IP', max_length=100)  # Field name made lowercase.
    comment_date = models.DateTimeField()
    comment_date_gmt = models.DateTimeField()
    comment_content = models.TextField()
    comment_karma = models.IntegerField()
    comment_approved = models.CharField(max_length=20)
    comment_agent = models.CharField(max_length=255)
    comment_type = models.CharField(max_length=20)
    comment_parent = models.PositiveBigIntegerField()
    user_id = models.PositiveBigIntegerField()

    class Meta:
        managed = False
        db_table = 'ori_wp_comments'


class OriWpPostmeta(models.Model):
    meta_id = models.BigAutoField(primary_key=True)
    post_id = models.PositiveBigIntegerField()
    meta_key = models.CharField(max_length=255, blank=True, null=True)
    meta_value = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ori_wp_postmeta'


class OriWpPosts(models.Model):
    id = models.BigAutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    post_author = models.PositiveBigIntegerField()
    post_date = models.DateTimeField()
    post_date_gmt = models.DateTimeField()
    post_content = models.TextField()
    post_title = models.TextField()
    post_excerpt = models.TextField()
    post_status = models.CharField(max_length=20)
    comment_status = models.CharField(max_length=20)
    ping_status = models.CharField(max_length=20)
    post_password = models.CharField(max_length=20)
    post_name = models.CharField(max_length=200)
    to_ping = models.TextField()
    pinged = models.TextField()
    post_modified = models.DateTimeField()
    post_modified_gmt = models.DateTimeField()
    post_content_filtered = models.TextField()
    post_parent = models.PositiveBigIntegerField()
    guid = models.CharField(max_length=255)
    menu_order = models.IntegerField()
    post_type = models.CharField(max_length=20)
    post_mime_type = models.CharField(max_length=100)
    comment_count = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'ori_wp_posts'


class OriWpUsermeta(models.Model):
    umeta_id = models.BigAutoField(primary_key=True)
    user_id = models.PositiveBigIntegerField()
    meta_key = models.CharField(max_length=255, blank=True, null=True)
    meta_value = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ori_wp_usermeta'


class OriWpUsers(models.Model):
    id = models.BigAutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    user_login = models.CharField(max_length=60)
    user_pass = models.CharField(max_length=64)
    user_nicename = models.CharField(max_length=50)
    user_email = models.CharField(max_length=100)
    user_url = models.CharField(max_length=100)
    user_registered = models.DateTimeField()
    user_activation_key = models.CharField(max_length=60)
    user_status = models.IntegerField()
    display_name = models.CharField(max_length=250)

    class Meta:
        managed = False
        db_table = 'ori_wp_users'


class PushnotificationMessage(models.Model):
    id = models.BigAutoField(primary_key=True)
    title = models.CharField(max_length=50)
    content = models.CharField(max_length=85)
    url = models.CharField(max_length=255)
    avatar = models.CharField(max_length=255)
    schedule = models.DateTimeField(blank=True, null=True)
    is_active = models.IntegerField()
    created_at = models.DateTimeField()
    created_by = models.CharField(max_length=100)
    updated_at = models.DateTimeField(blank=True, null=True)
    updated_by = models.CharField(max_length=100, blank=True, null=True)
    has_sent = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'pushnotification_message'


class PushnotificationSubscriber(models.Model):
    id = models.BigAutoField(primary_key=True)
    code = models.CharField(max_length=255)
    endpoint = models.TextField()
    member = models.CharField(max_length=11, blank=True, null=True)
    last_sent = models.DateTimeField(blank=True, null=True)
    is_active = models.IntegerField()
    created_at = models.DateTimeField()
    created_by = models.CharField(max_length=100)
    updated_at = models.DateTimeField(blank=True, null=True)
    updated_by = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pushnotification_subscriber'


class ResearchDownloadCooperations(models.Model):
    id = models.BigAutoField(primary_key=True)
    post_id = models.BigIntegerField()
    user_id = models.BigIntegerField()
    is_checked = models.IntegerField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'research_download_cooperations'


class SchedulePost(models.Model):
    master_schedule_post_id = models.IntegerField(blank=True, null=True)
    article_id = models.IntegerField(blank=True, null=True)
    article_title = models.CharField(max_length=255, blank=True, null=True)
    article_excerpt = models.TextField(blank=True, null=True)
    article_slug = models.CharField(max_length=255, blank=True, null=True)
    article_url = models.TextField(blank=True, null=True)
    article_thumbnail = models.TextField(blank=True, null=True)
    article_date = models.DateTimeField(blank=True, null=True)
    post_time = models.DateTimeField(blank=True, null=True)
    is_post = models.IntegerField(blank=True, null=True)
    attach_image = models.IntegerField(blank=True, null=True)
    type = models.CharField(max_length=100, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    created_by = models.CharField(max_length=125, blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    updated_by = models.CharField(max_length=125, blank=True, null=True)
    deleted = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'schedule_post'


class SgiAdmin(models.Model):
    admin_id = models.AutoField(primary_key=True)
    admin_username = models.CharField(max_length=30, blank=True, null=True)
    admin_password = models.CharField(max_length=250, blank=True, null=True)
    admin_name = models.CharField(max_length=20, blank=True, null=True)
    admin_level = models.IntegerField(blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    xxx = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sgi_admin'


class SgiNewsreader(models.Model):
    article_id = models.AutoField(primary_key=True)
    article_title = models.CharField(max_length=100, blank=True, null=True)
    article_url = models.CharField(max_length=150, blank=True, null=True)
    article_slug = models.CharField(max_length=150, blank=True, null=True)
    article_excerpt = models.TextField(blank=True, null=True)
    article_desc = models.TextField(blank=True, null=True)
    article_img = models.CharField(max_length=500, blank=True, null=True)
    article_publish = models.DateTimeField(blank=True, null=True)
    article_author = models.CharField(max_length=20, blank=True, null=True)
    article_category = models.CharField(max_length=50, blank=True, null=True)
    article_sub_category = models.CharField(max_length=20, blank=True, null=True)
    article_media = models.CharField(max_length=50, blank=True, null=True)
    article_media_url = models.CharField(max_length=150, blank=True, null=True)
    post_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sgi_newsreader'


class SgiNewsreaderDev(models.Model):
    article_id = models.AutoField(primary_key=True)
    article_title = models.CharField(max_length=100, blank=True, null=True)
    article_url = models.CharField(max_length=150, blank=True, null=True)
    article_slug = models.CharField(max_length=150, blank=True, null=True)
    article_excerpt = models.TextField(blank=True, null=True)
    article_desc = models.TextField(blank=True, null=True)
    article_img = models.CharField(max_length=500, blank=True, null=True)
    article_publish = models.DateTimeField(blank=True, null=True)
    article_author = models.CharField(max_length=20, blank=True, null=True)
    article_category = models.CharField(max_length=50, blank=True, null=True)
    article_sub_category = models.CharField(max_length=20, blank=True, null=True)
    article_media = models.CharField(max_length=50, blank=True, null=True)
    article_media_url = models.CharField(max_length=150, blank=True, null=True)
    post_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sgi_newsreader_dev'


class SgiNewsreaderTmp(models.Model):
    article_id = models.AutoField(primary_key=True)
    article_title = models.CharField(max_length=100, blank=True, null=True)
    article_url = models.CharField(max_length=150, blank=True, null=True)
    article_slug = models.CharField(max_length=150, blank=True, null=True)
    article_excerpt = models.TextField(blank=True, null=True)
    article_desc = models.TextField(blank=True, null=True)
    article_img = models.CharField(max_length=500, blank=True, null=True)
    article_publish = models.DateTimeField(blank=True, null=True)
    article_author = models.CharField(max_length=20, blank=True, null=True)
    article_category = models.CharField(max_length=50, blank=True, null=True)
    article_sub_category = models.CharField(max_length=20, blank=True, null=True)
    article_media = models.CharField(max_length=50, blank=True, null=True)
    article_media_url = models.CharField(max_length=150, blank=True, null=True)
    post_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sgi_newsreader_tmp'


class SgiPin(models.Model):
    pin_id = models.AutoField(primary_key=True)
    article_id = models.IntegerField(blank=True, null=True)
    channel = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sgi_pin'


class SsDailysocial(models.Model):
    ss_id = models.AutoField(primary_key=True)
    ss_category = models.CharField(max_length=50, blank=True, null=True)
    ss_url = models.CharField(max_length=150, blank=True, null=True)
    ss_isactive = models.IntegerField(blank=True, null=True)
    post_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ss_dailysocial'


class SsHybrid(models.Model):
    ss_id = models.AutoField(primary_key=True)
    ss_category = models.CharField(max_length=50, blank=True, null=True)
    ss_url = models.CharField(max_length=150, blank=True, null=True)
    ss_isactive = models.IntegerField(blank=True, null=True)
    post_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ss_hybrid'


class SubscriptionFeatures(models.Model):
    feature_id = models.BigAutoField(primary_key=True)
    feature_name = models.CharField(max_length=60)
    feature_slug = models.CharField(max_length=60, blank=True, null=True)
    is_active = models.IntegerField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'subscription_features'


class SubscriptionLogArticles(models.Model):
    id = models.BigAutoField(primary_key=True)
    post_id = models.BigIntegerField()
    user_id = models.BigIntegerField()
    post_title = models.TextField()
    post_slug = models.TextField()
    post_category = models.CharField(max_length=50)
    post_tag = models.CharField(max_length=255, blank=True, null=True)
    post_author_name = models.CharField(max_length=50)
    type = models.CharField(max_length=20)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'subscription_log_articles'


class SubscriptionLogEmailPayments(models.Model):
    email_id = models.BigAutoField(primary_key=True)
    order = models.ForeignKey('SubscriptionOrders', models.DO_NOTHING)
    payment_status = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'subscription_log_email_payments'


class SubscriptionOrders(models.Model):
    order_id = models.BigAutoField(primary_key=True)
    user_id = models.BigIntegerField()
    voucher = models.ForeignKey('SubscriptionVouchers', models.DO_NOTHING, blank=True, null=True)
    order_number = models.TextField()
    gross_amount = models.IntegerField(blank=True, null=True)
    payment_method = models.CharField(max_length=60, blank=True, null=True)
    payment_amount = models.IntegerField(blank=True, null=True)
    payment_status = models.IntegerField(blank=True, null=True)
    order_details = models.TextField(blank=True, null=True)
    payment_details = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'subscription_orders'


class SubscriptionPlanFeatures(models.Model):
    is_checked = models.IntegerField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    feature = models.OneToOneField(SubscriptionFeatures, models.DO_NOTHING, primary_key=True)
    plan = models.ForeignKey('SubscriptionPlans', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'subscription_plan_features'
        unique_together = (('feature', 'plan'),)


class SubscriptionPlans(models.Model):
    plan_id = models.BigAutoField(primary_key=True)
    plan_name = models.CharField(max_length=60)
    plan_slug = models.CharField(max_length=60, blank=True, null=True)
    plan_duration = models.CharField(max_length=60)
    validity_days = models.IntegerField()
    price = models.IntegerField()
    plan_details = models.TextField(blank=True, null=True)
    is_active = models.IntegerField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'subscription_plans'


class SubscriptionVouchers(models.Model):
    id = models.BigAutoField(primary_key=True)
    code = models.CharField(max_length=60)
    name = models.CharField(max_length=60, blank=True, null=True)
    slug = models.CharField(max_length=60)
    description = models.TextField(blank=True, null=True)
    uses = models.IntegerField()
    max_uses = models.IntegerField()
    discount_amount = models.IntegerField()
    is_percentage = models.IntegerField()
    starts_at = models.DateField(blank=True, null=True)
    expires_at = models.DateField(blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'subscription_vouchers'


class SubscriptionVouchersPlans(models.Model):
    status = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    plan = models.OneToOneField(SubscriptionPlans, models.DO_NOTHING, primary_key=True)
    voucher = models.ForeignKey(SubscriptionVouchers, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'subscription_vouchers_plans'
        unique_together = (('plan', 'voucher'), ('plan', 'voucher'),)


class SubscriptionVouchersRedeems(models.Model):
    is_take = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    user_id = models.BigIntegerField(primary_key=True)
    voucher = models.ForeignKey(SubscriptionVouchers, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'subscription_vouchers_redeems'
        unique_together = (('user_id', 'voucher'), ('user_id', 'voucher'),)


class Subscriptions(models.Model):
    subscription_id = models.BigAutoField(primary_key=True)
    user_id = models.BigIntegerField()
    plan = models.ForeignKey(SubscriptionPlans, models.DO_NOTHING)
    order = models.OneToOneField(SubscriptionOrders, models.DO_NOTHING)
    is_active = models.IntegerField()
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'subscriptions'


class TableModify(models.Model):
    id = models.BigAutoField(primary_key=True)
    container = models.CharField(max_length=100)
    container_id = models.CharField(max_length=100)
    updated_value = models.TextField()
    is_active = models.IntegerField()
    created_at = models.DateTimeField()
    created_by = models.CharField(max_length=100)
    updated_at = models.DateTimeField(blank=True, null=True)
    updated_by = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'table_modify'


class TrikinetCover(models.Model):
    cover_id = models.AutoField(primary_key=True)
    cover_title = models.CharField(max_length=100, blank=True, null=True)
    cover_img = models.CharField(max_length=200, blank=True, null=True)
    cover_tag = models.CharField(max_length=50, blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    post_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'trikinet_cover'


class UserDownload(models.Model):
    id = models.BigAutoField(primary_key=True)
    user_id = models.IntegerField()
    post_id = models.IntegerField()
    is_active = models.IntegerField()
    created_at = models.DateTimeField()
    created_by = models.CharField(max_length=100)
    updated_at = models.DateTimeField(blank=True, null=True)
    updated_by = models.CharField(max_length=100, blank=True, null=True)
    info = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user_download'


class UserInbox(models.Model):
    id = models.BigAutoField(primary_key=True)
    userid = models.IntegerField(blank=True, null=True)
    subject = models.CharField(max_length=100)
    message = models.TextField()
    inboxfrom = models.CharField(max_length=200)
    is_read = models.IntegerField()
    is_active = models.IntegerField()
    created_at = models.DateTimeField()
    created_by = models.CharField(max_length=100)
    updated_at = models.DateTimeField(blank=True, null=True)
    updated_by = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user_inbox'


class WpWpSeo404Links(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    ctime = models.DateTimeField()
    link = models.CharField(unique=True, max_length=255, db_collation='utf8_unicode_ci')
    referrer = models.CharField(max_length=255, db_collation='utf8_unicode_ci')
    ip = models.CharField(max_length=20, db_collation='utf8_unicode_ci')
    country = models.CharField(max_length=100, db_collation='utf8_unicode_ci')
    os = models.CharField(max_length=20, db_collation='utf8_unicode_ci')
    browser = models.CharField(max_length=20, db_collation='utf8_unicode_ci')

    class Meta:
        managed = False
        db_table = 'wp_WP_SEO_404_links'


class WpWpSeoCache(models.Model):
    id = models.PositiveIntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    is_redirected = models.PositiveIntegerField()
    redirect_from = models.CharField(max_length=255, db_collation='utf8_unicode_ci')
    redirect_to = models.CharField(max_length=255, db_collation='utf8_unicode_ci')
    redirect_type = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'wp_WP_SEO_Cache'


class WpWpSeoRedirection(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    enabled = models.IntegerField()
    redirect_from = models.CharField(unique=True, max_length=255, db_collation='utf8_unicode_ci')
    redirect_from_type = models.CharField(max_length=255, db_collation='utf8_unicode_ci')
    redirect_from_folder_settings = models.IntegerField()
    redirect_from_subfolders = models.IntegerField()
    redirect_to = models.CharField(max_length=255, db_collation='utf8_unicode_ci')
    redirect_to_type = models.CharField(max_length=255, db_collation='utf8_unicode_ci')
    redirect_to_folder_settings = models.IntegerField()
    regex = models.CharField(max_length=255, db_collation='utf8_unicode_ci')
    redirect_type = models.CharField(max_length=255, db_collation='utf8_unicode_ci')
    url_type = models.IntegerField()
    postid = models.PositiveIntegerField(db_column='postID', blank=True, null=True)  # Field name made lowercase.
    import_flag = models.IntegerField()
    hits = models.PositiveIntegerField()
    access_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'wp_WP_SEO_Redirection'


class WpWpSeoRedirectionLog(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    rid = models.PositiveIntegerField(db_column='rID', blank=True, null=True)  # Field name made lowercase.
    postid = models.PositiveIntegerField(db_column='postID', blank=True, null=True)  # Field name made lowercase.
    ctime = models.DateTimeField()
    rfrom = models.CharField(max_length=255, db_collation='utf8_unicode_ci')
    rto = models.CharField(max_length=255, db_collation='utf8_unicode_ci')
    rtype = models.CharField(max_length=255, db_collation='utf8_unicode_ci')
    rsrc = models.CharField(max_length=20, db_collation='utf8_unicode_ci')
    referrer = models.CharField(max_length=255, db_collation='utf8_unicode_ci')
    ip = models.CharField(max_length=20, db_collation='utf8_unicode_ci')
    country = models.CharField(max_length=100, db_collation='utf8_unicode_ci')
    os = models.CharField(max_length=20, db_collation='utf8_unicode_ci')
    browser = models.CharField(max_length=20, db_collation='utf8_unicode_ci')

    class Meta:
        managed = False
        db_table = 'wp_WP_SEO_Redirection_LOG'


class WpActionschedulerActions(models.Model):
    action_id = models.BigAutoField(primary_key=True)
    hook = models.CharField(max_length=191)
    status = models.CharField(max_length=20)
    scheduled_date_gmt = models.DateTimeField()
    scheduled_date_local = models.DateTimeField()
    args = models.CharField(max_length=191, blank=True, null=True)
    schedule = models.TextField(blank=True, null=True)
    group_id = models.PositiveBigIntegerField()
    attempts = models.IntegerField()
    last_attempt_gmt = models.DateTimeField()
    last_attempt_local = models.DateTimeField()
    claim_id = models.PositiveBigIntegerField()
    extended_args = models.CharField(max_length=8000, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'wp_actionscheduler_actions'


class WpActionschedulerClaims(models.Model):
    claim_id = models.BigAutoField(primary_key=True)
    date_created_gmt = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'wp_actionscheduler_claims'


class WpActionschedulerGroups(models.Model):
    group_id = models.BigAutoField(primary_key=True)
    slug = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'wp_actionscheduler_groups'


class WpActionschedulerLogs(models.Model):
    log_id = models.BigAutoField(primary_key=True)
    action_id = models.PositiveBigIntegerField()
    message = models.TextField()
    log_date_gmt = models.DateTimeField()
    log_date_local = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'wp_actionscheduler_logs'


class WpBvActivitiesStore(models.Model):
    id = models.BigAutoField(primary_key=True)
    site_id = models.IntegerField()
    user_id = models.IntegerField(blank=True, null=True)
    username = models.TextField(blank=True, null=True)
    request_id = models.TextField(blank=True, null=True)
    ip = models.CharField(max_length=20, blank=True, null=True)
    event_type = models.CharField(max_length=40)
    event_data = models.TextField()
    time = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'wp_bv_activities_store'


class WpCfFormEntries(models.Model):
    form_id = models.CharField(max_length=18)
    user_id = models.IntegerField()
    datestamp = models.DateTimeField()
    status = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'wp_cf_form_entries'


class WpCfFormEntryMeta(models.Model):
    meta_id = models.BigAutoField(primary_key=True)
    entry_id = models.PositiveBigIntegerField()
    process_id = models.CharField(max_length=255, blank=True, null=True)
    meta_key = models.CharField(max_length=255, blank=True, null=True)
    meta_value = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'wp_cf_form_entry_meta'


class WpCfFormEntryValues(models.Model):
    entry_id = models.IntegerField()
    field_id = models.CharField(max_length=20)
    slug = models.CharField(max_length=255)
    value = models.TextField()

    class Meta:
        managed = False
        db_table = 'wp_cf_form_entry_values'


class WpCommentmeta(models.Model):
    meta_id = models.BigAutoField(primary_key=True)
    comment_id = models.PositiveBigIntegerField()
    meta_key = models.CharField(max_length=255, blank=True, null=True)
    meta_value = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'wp_commentmeta'


class WpComments(models.Model):
    comment_id = models.BigAutoField(db_column='comment_ID', primary_key=True)  # Field name made lowercase.
    comment_post_id = models.PositiveBigIntegerField(db_column='comment_post_ID')  # Field name made lowercase.
    comment_author = models.TextField()
    comment_author_email = models.CharField(max_length=100)
    comment_author_url = models.CharField(max_length=200)
    comment_author_ip = models.CharField(db_column='comment_author_IP', max_length=100)  # Field name made lowercase.
    comment_date = models.DateTimeField()
    comment_date_gmt = models.DateTimeField()
    comment_content = models.TextField()
    comment_karma = models.IntegerField()
    comment_approved = models.CharField(max_length=20)
    comment_agent = models.CharField(max_length=255)
    comment_type = models.CharField(max_length=20)
    comment_parent = models.PositiveBigIntegerField()
    user_id = models.PositiveBigIntegerField()

    class Meta:
        managed = False
        db_table = 'wp_comments'


class WpEbdItem(models.Model):
    download_id = models.CharField(max_length=128, blank=True, null=True)
    file = models.CharField(max_length=255, blank=True, null=True)
    title = models.CharField(max_length=255, db_collation='utf8_unicode_ci', blank=True, null=True)
    timestamp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'wp_ebd_item'


class WpEbdLink(models.Model):
    id = models.AutoField(unique=True, primary_key=True)
    item_id = models.IntegerField()
    is_downloaded = models.SmallIntegerField()
    email = models.CharField(max_length=128)
    expire_time = models.BigIntegerField(blank=True, null=True)
    time_requested = models.BigIntegerField(blank=True, null=True)
    uid = models.CharField(max_length=255)
    selected_id = models.BigIntegerField()
    delivered_as = models.CharField(max_length=255, blank=True, null=True)
    is_masked = models.CharField(max_length=4, blank=True, null=True)
    is_force_download = models.CharField(max_length=4, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'wp_ebd_link'


class WpEbdPostedData(models.Model):
    time_requested = models.BigIntegerField(unique=True, blank=True, null=True)
    email = models.CharField(max_length=128, blank=True, null=True)
    user_name = models.CharField(max_length=128, db_collation='utf8_unicode_ci', blank=True, null=True)
    posted_data = models.TextField()

    class Meta:
        managed = False
        db_table = 'wp_ebd_posted_data'


class WpFormmaker(models.Model):
    title = models.CharField(max_length=127)
    mail = models.CharField(max_length=128)
    form_front = models.TextField()
    theme = models.IntegerField()
    javascript = models.TextField()
    submit_text = models.TextField()
    url = models.CharField(max_length=200)
    submit_text_type = models.IntegerField()
    script_mail = models.TextField()
    script_mail_user = models.TextField()
    counter = models.IntegerField()
    published = models.IntegerField()
    label_order = models.TextField()
    label_order_current = models.TextField()
    article_id = models.CharField(max_length=500)
    pagination = models.CharField(max_length=128)
    show_title = models.CharField(max_length=128)
    show_numbers = models.CharField(max_length=128)
    public_key = models.CharField(max_length=50)
    private_key = models.CharField(max_length=50)
    recaptcha_theme = models.CharField(max_length=20)
    paypal_mode = models.IntegerField()
    checkout_mode = models.CharField(max_length=20)
    paypal_email = models.CharField(max_length=50)
    payment_currency = models.CharField(max_length=20)
    tax = models.FloatField()
    form_fields = models.TextField()
    savedb = models.IntegerField()
    sendemail = models.IntegerField()
    requiredmark = models.CharField(max_length=20)
    from_mail = models.CharField(max_length=128)
    from_name = models.CharField(max_length=128)
    reply_to = models.CharField(max_length=128)
    send_to = models.CharField(max_length=128)
    autogen_layout = models.IntegerField()
    custom_front = models.TextField()
    mail_from_user = models.CharField(max_length=128)
    mail_from_name_user = models.CharField(max_length=128)
    reply_to_user = models.CharField(max_length=128)
    condition = models.TextField()
    mail_cc = models.CharField(max_length=128)
    mail_cc_user = models.CharField(max_length=128)
    mail_bcc = models.CharField(max_length=128)
    mail_bcc_user = models.CharField(max_length=128)
    mail_subject = models.CharField(max_length=128)
    mail_subject_user = models.CharField(max_length=128)
    mail_mode = models.IntegerField()
    mail_mode_user = models.IntegerField()
    mail_attachment = models.IntegerField()
    mail_attachment_user = models.IntegerField()
    user_id_wd = models.CharField(max_length=220)
    sortable = models.IntegerField()
    frontend_submit_fields = models.TextField()
    frontend_submit_stat_fields = models.TextField()
    mail_emptyfields = models.IntegerField()
    mail_verify = models.IntegerField()
    mail_verify_expiretime = models.FloatField()
    mail_verification_post_id = models.IntegerField()
    save_uploads = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'wp_formmaker'


class WpFormmakerBackup(models.Model):
    backup_id = models.AutoField(primary_key=True)
    cur = models.IntegerField()
    id = models.IntegerField()
    title = models.CharField(max_length=127)
    mail = models.CharField(max_length=128)
    form_front = models.TextField()
    theme = models.IntegerField()
    javascript = models.TextField()
    submit_text = models.TextField()
    url = models.CharField(max_length=200)
    submit_text_type = models.IntegerField()
    script_mail = models.TextField()
    script_mail_user = models.TextField()
    counter = models.IntegerField()
    published = models.IntegerField()
    label_order = models.TextField()
    label_order_current = models.TextField()
    article_id = models.CharField(max_length=500)
    pagination = models.CharField(max_length=128)
    show_title = models.CharField(max_length=128)
    show_numbers = models.CharField(max_length=128)
    public_key = models.CharField(max_length=50)
    private_key = models.CharField(max_length=50)
    recaptcha_theme = models.CharField(max_length=20)
    paypal_mode = models.IntegerField()
    checkout_mode = models.CharField(max_length=20)
    paypal_email = models.CharField(max_length=50)
    payment_currency = models.CharField(max_length=20)
    tax = models.FloatField()
    form_fields = models.TextField()
    savedb = models.IntegerField()
    sendemail = models.IntegerField()
    requiredmark = models.CharField(max_length=20)
    from_mail = models.CharField(max_length=128)
    from_name = models.CharField(max_length=128)
    reply_to = models.CharField(max_length=128)
    send_to = models.CharField(max_length=128)
    autogen_layout = models.IntegerField()
    custom_front = models.TextField()
    mail_from_user = models.CharField(max_length=128)
    mail_from_name_user = models.CharField(max_length=128)
    reply_to_user = models.CharField(max_length=128)
    condition = models.TextField()
    mail_cc = models.CharField(max_length=128)
    mail_cc_user = models.CharField(max_length=128)
    mail_bcc = models.CharField(max_length=128)
    mail_bcc_user = models.CharField(max_length=128)
    mail_subject = models.CharField(max_length=128)
    mail_subject_user = models.CharField(max_length=128)
    mail_mode = models.IntegerField()
    mail_mode_user = models.IntegerField()
    mail_attachment = models.IntegerField()
    mail_attachment_user = models.IntegerField()
    user_id_wd = models.CharField(max_length=220)
    sortable = models.IntegerField()
    frontend_submit_fields = models.TextField()
    frontend_submit_stat_fields = models.TextField()
    mail_emptyfields = models.IntegerField()
    mail_verify = models.IntegerField()
    mail_verify_expiretime = models.FloatField()
    mail_verification_post_id = models.IntegerField()
    save_uploads = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'wp_formmaker_backup'


class WpFormmakerBlocked(models.Model):
    ip = models.CharField(max_length=128)

    class Meta:
        managed = False
        db_table = 'wp_formmaker_blocked'


class WpFormmakerQuery(models.Model):
    form_id = models.IntegerField()
    query = models.TextField()
    details = models.TextField()

    class Meta:
        managed = False
        db_table = 'wp_formmaker_query'


class WpFormmakerSessions(models.Model):
    form_id = models.IntegerField()
    group_id = models.IntegerField()
    ip = models.CharField(max_length=20)
    ord_date = models.DateTimeField()
    ord_last_modified = models.DateTimeField()
    status = models.CharField(max_length=50)
    full_name = models.CharField(max_length=100)
    email = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    mobile_phone = models.CharField(max_length=255)
    fax = models.CharField(max_length=255)
    address = models.CharField(max_length=300)
    paypal_info = models.TextField()
    without_paypal_info = models.TextField()
    ipn = models.CharField(max_length=20)
    checkout_method = models.CharField(max_length=20)
    tax = models.FloatField()
    shipping = models.FloatField()
    shipping_type = models.CharField(max_length=200)
    read = models.IntegerField()
    total = models.FloatField()
    currency = models.CharField(max_length=24)

    class Meta:
        managed = False
        db_table = 'wp_formmaker_sessions'


class WpFormmakerSubmits(models.Model):
    form_id = models.IntegerField()
    element_label = models.CharField(max_length=128)
    element_value = models.CharField(max_length=600)
    group_id = models.IntegerField()
    date = models.DateTimeField()
    ip = models.CharField(max_length=32)
    user_id_wd = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'wp_formmaker_submits'


class WpFormmakerThemes(models.Model):
    title = models.CharField(max_length=200)
    css = models.TextField()
    default = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'wp_formmaker_themes'


class WpFormmakerViews(models.Model):
    form_id = models.IntegerField(primary_key=True)
    views = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'wp_formmaker_views'


class WpHugeItContactContacts(models.Model):
    name = models.CharField(max_length=200)
    hc_acceptms = models.TextField(blank=True, null=True)
    hc_width = models.PositiveIntegerField(blank=True, null=True)
    hc_userms = models.TextField(blank=True, null=True)
    hc_yourstyle = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    param = models.TextField(blank=True, null=True)
    ordering = models.IntegerField()
    published = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'wp_huge_it_contact_contacts'


class WpHugeItContactContactsFields(models.Model):
    name = models.TextField(blank=True, null=True)
    hugeit_contact_id = models.CharField(max_length=200, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    conttype = models.TextField()
    hc_field_label = models.TextField(blank=True, null=True)
    hc_other_field = models.CharField(max_length=128, blank=True, null=True)
    field_type = models.TextField()
    hc_required = models.TextField()
    ordering = models.IntegerField()
    published = models.PositiveIntegerField(blank=True, null=True)
    hc_input_show_default = models.TextField()
    hc_left_right = models.TextField()

    class Meta:
        managed = False
        db_table = 'wp_huge_it_contact_contacts_fields'


class WpHugeItContactGeneralOptions(models.Model):
    name = models.CharField(max_length=50)
    title = models.CharField(max_length=200)
    description = models.TextField()
    value = models.TextField()

    class Meta:
        managed = False
        db_table = 'wp_huge_it_contact_general_options'


class WpHugeItContactStyleFields(models.Model):
    name = models.CharField(max_length=50)
    title = models.CharField(max_length=200)
    description = models.TextField()
    options_name = models.TextField()
    value = models.CharField(max_length=200)

    class Meta:
        managed = False
        db_table = 'wp_huge_it_contact_style_fields'


class WpHugeItContactStyles(models.Model):
    name = models.CharField(max_length=50)
    last_update = models.CharField(max_length=50)
    ordering = models.IntegerField()
    published = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'wp_huge_it_contact_styles'


class WpHugeItContactSubmission(models.Model):
    contact_id = models.IntegerField()
    sub_labels = models.TextField()
    submission = models.TextField()
    submission_date = models.TextField()
    submission_ip = models.TextField()
    customer_country = models.TextField()
    customer_spam = models.TextField()
    customer_read_or_not = models.TextField()
    files_url = models.TextField(blank=True, null=True)
    files_type = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'wp_huge_it_contact_submission'


class WpHugeItContactSubscribers(models.Model):
    subscriber_id = models.AutoField(primary_key=True)
    subscriber_form_id = models.IntegerField()
    subscriber_email = models.CharField(max_length=50)
    text = models.TextField()
    send = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'wp_huge_it_contact_subscribers'


class WpLinks(models.Model):
    link_id = models.BigAutoField(primary_key=True)
    link_url = models.CharField(max_length=255)
    link_name = models.CharField(max_length=255)
    link_image = models.CharField(max_length=255)
    link_target = models.CharField(max_length=25)
    link_description = models.CharField(max_length=255)
    link_visible = models.CharField(max_length=20)
    link_owner = models.PositiveBigIntegerField()
    link_rating = models.IntegerField()
    link_updated = models.DateTimeField()
    link_rel = models.CharField(max_length=255)
    link_notes = models.TextField()
    link_rss = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'wp_links'


class WpMsSnippets(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.TextField()
    description = models.TextField()
    code = models.TextField()
    tags = models.TextField()
    scope = models.CharField(max_length=15)
    priority = models.SmallIntegerField()
    active = models.IntegerField()
    modified = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'wp_ms_snippets'


class WpNxsLog(models.Model):
    id = models.BigAutoField(unique=True, primary_key=True)
    date = models.DateTimeField()
    act = models.CharField(max_length=255)
    nt = models.CharField(max_length=255)
    type = models.CharField(max_length=255)
    msg = models.TextField()
    extinfo = models.TextField(db_column='extInfo', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'wp_nxs_log'


class WpOptions(models.Model):
    option_id = models.BigAutoField(primary_key=True)
    option_name = models.CharField(unique=True, max_length=191, blank=True, null=True)
    option_value = models.TextField()
    autoload = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'wp_options'


class WpPmxeExports(models.Model):
    id = models.BigAutoField(primary_key=True)
    parent_id = models.BigIntegerField()
    attch_id = models.BigIntegerField()
    options = models.TextField(blank=True, null=True)
    scheduled = models.CharField(max_length=64)
    registered_on = models.DateTimeField()
    friendly_name = models.TextField()
    exported = models.BigIntegerField()
    canceled = models.IntegerField()
    canceled_on = models.DateTimeField()
    settings_update_on = models.DateTimeField()
    last_activity = models.DateTimeField()
    processing = models.IntegerField()
    executing = models.IntegerField()
    triggered = models.IntegerField()
    iteration = models.BigIntegerField()
    export_post_type = models.TextField()

    class Meta:
        managed = False
        db_table = 'wp_pmxe_exports'


class WpPmxeGoogleCats(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=200)
    parent_id = models.IntegerField()
    parent_name = models.CharField(max_length=200)
    level = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'wp_pmxe_google_cats'


class WpPmxePosts(models.Model):
    id = models.BigAutoField(primary_key=True)
    post_id = models.PositiveBigIntegerField()
    export_id = models.PositiveBigIntegerField()
    iteration = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'wp_pmxe_posts'


class WpPmxeTemplates(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=200)
    options = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'wp_pmxe_templates'


class WpPostmeta(models.Model):
    meta_id = models.BigAutoField(primary_key=True)
    post_id = models.PositiveBigIntegerField()
    meta_key = models.CharField(max_length=255, blank=True, null=True)
    meta_value = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'wp_postmeta'


class WpPosts(models.Model):
    id = models.BigAutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    post_author = models.PositiveBigIntegerField()
    post_date = models.DateTimeField()
    post_date_gmt = models.DateTimeField()
    post_content = models.TextField()
    post_title = models.TextField()
    post_excerpt = models.TextField()
    post_status = models.CharField(max_length=20)
    comment_status = models.CharField(max_length=20)
    ping_status = models.CharField(max_length=20)
    post_password = models.CharField(max_length=255)
    post_name = models.CharField(max_length=200)
    to_ping = models.TextField()
    pinged = models.TextField()
    post_modified = models.DateTimeField()
    post_modified_gmt = models.DateTimeField()
    post_content_filtered = models.TextField()
    post_parent = models.PositiveBigIntegerField()
    guid = models.CharField(max_length=255)
    menu_order = models.IntegerField()
    post_type = models.CharField(max_length=20)
    post_mime_type = models.CharField(max_length=100)
    comment_count = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'wp_posts'


class WpSnippets(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.TextField()
    description = models.TextField()
    code = models.TextField()
    tags = models.TextField()
    scope = models.CharField(max_length=15)
    priority = models.SmallIntegerField()
    active = models.IntegerField()
    modified = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'wp_snippets'


class WpTermRelationships(models.Model):
    object_id = models.PositiveBigIntegerField(primary_key=True)
    term_taxonomy_id = models.PositiveBigIntegerField()
    term_order = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'wp_term_relationships'
        unique_together = (('object_id', 'term_taxonomy_id'),)


class WpTermTaxonomy(models.Model):
    term_taxonomy_id = models.BigAutoField(primary_key=True)
    term_id = models.PositiveBigIntegerField()
    taxonomy = models.CharField(max_length=32)
    description = models.TextField()
    parent = models.PositiveBigIntegerField()
    count = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'wp_term_taxonomy'
        unique_together = (('term_id', 'taxonomy'),)


class WpTermmeta(models.Model):
    meta_id = models.BigAutoField(primary_key=True)
    term_id = models.PositiveBigIntegerField()
    meta_key = models.CharField(max_length=255, blank=True, null=True)
    meta_value = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'wp_termmeta'


class WpTerms(models.Model):
    term_id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=200)
    slug = models.CharField(max_length=200)
    term_group = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'wp_terms'


class WpUsermeta(models.Model):
    umeta_id = models.BigAutoField(primary_key=True)
    user_id = models.PositiveBigIntegerField()
    meta_key = models.CharField(max_length=255, blank=True, null=True)
    meta_value = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'wp_usermeta'


class WpUsers(models.Model):
    id = models.BigAutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    user_login = models.CharField(max_length=60)
    user_pass = models.CharField(max_length=255)
    user_nicename = models.CharField(max_length=50)
    user_email = models.CharField(max_length=100)
    user_url = models.CharField(max_length=100)
    user_registered = models.DateTimeField()
    user_activation_key = models.CharField(max_length=255)
    user_status = models.IntegerField()
    display_name = models.CharField(max_length=250)

    class Meta:
        managed = False
        db_table = 'wp_users'


class WpWfblockediplog(models.Model):
    ip = models.CharField(db_column='IP', primary_key=True, max_length=16)  # Field name made lowercase.
    countrycode = models.CharField(db_column='countryCode', max_length=2)  # Field name made lowercase.
    blockcount = models.PositiveIntegerField(db_column='blockCount')  # Field name made lowercase.
    unixday = models.PositiveIntegerField()
    blocktype = models.CharField(db_column='blockType', max_length=50)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'wp_wfblockediplog'
        unique_together = (('ip', 'unixday', 'blocktype'),)


class WpWfblocks7(models.Model):
    id = models.BigAutoField(primary_key=True)
    type = models.PositiveIntegerField()
    ip = models.CharField(db_column='IP', max_length=16)  # Field name made lowercase.
    blockedtime = models.BigIntegerField(db_column='blockedTime')  # Field name made lowercase.
    reason = models.CharField(max_length=255)
    lastattempt = models.PositiveIntegerField(db_column='lastAttempt', blank=True, null=True)  # Field name made lowercase.
    blockedhits = models.PositiveIntegerField(db_column='blockedHits', blank=True, null=True)  # Field name made lowercase.
    expiration = models.PositiveBigIntegerField()
    parameters = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'wp_wfblocks7'


class WpWfconfig(models.Model):
    name = models.CharField(primary_key=True, max_length=100)
    val = models.TextField(blank=True, null=True)
    autoload = models.CharField(max_length=3)

    class Meta:
        managed = False
        db_table = 'wp_wfconfig'


class WpWfcrawlers(models.Model):
    ip = models.CharField(db_column='IP', primary_key=True, max_length=16)  # Field name made lowercase.
    patternsig = models.CharField(db_column='patternSig', max_length=16)  # Field name made lowercase.
    status = models.CharField(max_length=8)
    lastupdate = models.PositiveIntegerField(db_column='lastUpdate')  # Field name made lowercase.
    ptr = models.CharField(db_column='PTR', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'wp_wfcrawlers'
        unique_together = (('ip', 'patternsig'),)


class WpWffilechanges(models.Model):
    filenamehash = models.CharField(db_column='filenameHash', primary_key=True, max_length=64)  # Field name made lowercase.
    file = models.CharField(max_length=1000)
    md5 = models.CharField(max_length=32)

    class Meta:
        managed = False
        db_table = 'wp_wffilechanges'


class WpWffilemods(models.Model):
    filenamemd5 = models.CharField(db_column='filenameMD5', primary_key=True, max_length=16)  # Field name made lowercase.
    filename = models.CharField(max_length=1000)
    knownfile = models.PositiveIntegerField(db_column='knownFile')  # Field name made lowercase.
    oldmd5 = models.CharField(db_column='oldMD5', max_length=16)  # Field name made lowercase.
    newmd5 = models.CharField(db_column='newMD5', max_length=16)  # Field name made lowercase.
    shac = models.CharField(db_column='SHAC', max_length=32)  # Field name made lowercase.
    stoppedonsignature = models.CharField(db_column='stoppedOnSignature', max_length=255)  # Field name made lowercase.
    stoppedonposition = models.PositiveIntegerField(db_column='stoppedOnPosition')  # Field name made lowercase.
    issafefile = models.CharField(db_column='isSafeFile', max_length=1)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'wp_wffilemods'


class WpWfhits(models.Model):
    attacklogtime = models.FloatField(db_column='attackLogTime')  # Field name made lowercase.
    ctime = models.FloatField()
    ip = models.CharField(db_column='IP', max_length=16, blank=True, null=True)  # Field name made lowercase.
    jsrun = models.IntegerField(db_column='jsRun', blank=True, null=True)  # Field name made lowercase.
    statuscode = models.IntegerField(db_column='statusCode')  # Field name made lowercase.
    isgoogle = models.IntegerField(db_column='isGoogle')  # Field name made lowercase.
    userid = models.PositiveIntegerField(db_column='userID')  # Field name made lowercase.
    newvisit = models.PositiveIntegerField(db_column='newVisit')  # Field name made lowercase.
    url = models.TextField(db_column='URL', blank=True, null=True)  # Field name made lowercase.
    referer = models.TextField(blank=True, null=True)
    ua = models.TextField(db_column='UA', blank=True, null=True)  # Field name made lowercase.
    action = models.CharField(max_length=64)
    actiondescription = models.TextField(db_column='actionDescription', blank=True, null=True)  # Field name made lowercase.
    actiondata = models.TextField(db_column='actionData', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'wp_wfhits'


class WpWfhoover(models.Model):
    owner = models.TextField(blank=True, null=True)
    host = models.TextField(blank=True, null=True)
    path = models.TextField(blank=True, null=True)
    hostkey = models.CharField(db_column='hostKey', max_length=124, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'wp_wfhoover'


class WpWfissues(models.Model):
    time = models.PositiveIntegerField()
    lastupdated = models.PositiveIntegerField(db_column='lastUpdated')  # Field name made lowercase.
    status = models.CharField(max_length=10)
    type = models.CharField(max_length=20)
    severity = models.PositiveIntegerField()
    ignorep = models.CharField(db_column='ignoreP', max_length=32)  # Field name made lowercase.
    ignorec = models.CharField(db_column='ignoreC', max_length=32)  # Field name made lowercase.
    shortmsg = models.CharField(db_column='shortMsg', max_length=255)  # Field name made lowercase.
    longmsg = models.TextField(db_column='longMsg', blank=True, null=True)  # Field name made lowercase.
    data = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'wp_wfissues'


class WpWfknownfilelist(models.Model):
    path = models.TextField()

    class Meta:
        managed = False
        db_table = 'wp_wfknownfilelist'


class WpWflivetraffichuman(models.Model):
    ip = models.CharField(db_column='IP', primary_key=True, max_length=16)  # Field name made lowercase.
    identifier = models.CharField(max_length=32)
    expiration = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'wp_wflivetraffichuman'
        unique_together = (('ip', 'identifier'),)


class WpWflocs(models.Model):
    ip = models.CharField(db_column='IP', primary_key=True, max_length=16)  # Field name made lowercase.
    ctime = models.PositiveIntegerField()
    failed = models.PositiveIntegerField()
    city = models.CharField(max_length=255, blank=True, null=True)
    region = models.CharField(max_length=255, blank=True, null=True)
    countryname = models.CharField(db_column='countryName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    countrycode = models.CharField(db_column='countryCode', max_length=2, blank=True, null=True)  # Field name made lowercase.
    lat = models.FloatField(blank=True, null=True)
    lon = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'wp_wflocs'


class WpWflogins(models.Model):
    hitid = models.IntegerField(db_column='hitID', blank=True, null=True)  # Field name made lowercase.
    ctime = models.FloatField()
    fail = models.PositiveIntegerField()
    action = models.CharField(max_length=40)
    username = models.CharField(max_length=255)
    userid = models.PositiveIntegerField(db_column='userID')  # Field name made lowercase.
    ip = models.CharField(db_column='IP', max_length=16, blank=True, null=True)  # Field name made lowercase.
    ua = models.TextField(db_column='UA', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'wp_wflogins'


class WpWfls2FaSecrets(models.Model):
    user_id = models.PositiveBigIntegerField()
    secret = models.TextField()
    recovery = models.TextField()
    ctime = models.PositiveIntegerField()
    vtime = models.PositiveIntegerField()
    mode = models.CharField(max_length=13)

    class Meta:
        managed = False
        db_table = 'wp_wfls_2fa_secrets'


class WpWflsSettings(models.Model):
    name = models.CharField(primary_key=True, max_length=191)
    value = models.TextField(blank=True, null=True)
    autoload = models.CharField(max_length=3)

    class Meta:
        managed = False
        db_table = 'wp_wfls_settings'


class WpWfnotifications(models.Model):
    id = models.CharField(primary_key=True, max_length=32)
    new = models.PositiveIntegerField()
    category = models.CharField(max_length=255)
    priority = models.IntegerField()
    ctime = models.PositiveIntegerField()
    html = models.TextField()
    links = models.TextField()

    class Meta:
        managed = False
        db_table = 'wp_wfnotifications'


class WpWfpendingissues(models.Model):
    time = models.PositiveIntegerField()
    lastupdated = models.PositiveIntegerField(db_column='lastUpdated')  # Field name made lowercase.
    status = models.CharField(max_length=10)
    type = models.CharField(max_length=20)
    severity = models.PositiveIntegerField()
    ignorep = models.CharField(db_column='ignoreP', max_length=32)  # Field name made lowercase.
    ignorec = models.CharField(db_column='ignoreC', max_length=32)  # Field name made lowercase.
    shortmsg = models.CharField(db_column='shortMsg', max_length=255)  # Field name made lowercase.
    longmsg = models.TextField(db_column='longMsg', blank=True, null=True)  # Field name made lowercase.
    data = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'wp_wfpendingissues'


class WpWfreversecache(models.Model):
    ip = models.CharField(db_column='IP', primary_key=True, max_length=16)  # Field name made lowercase.
    host = models.CharField(max_length=255)
    lastupdate = models.PositiveIntegerField(db_column='lastUpdate')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'wp_wfreversecache'


class WpWfsnipcache(models.Model):
    ip = models.CharField(db_column='IP', max_length=45)  # Field name made lowercase.
    expiration = models.DateTimeField()
    body = models.CharField(max_length=255)
    count = models.PositiveIntegerField()
    type = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'wp_wfsnipcache'


class WpWfstatus(models.Model):
    id = models.BigAutoField(primary_key=True)
    ctime = models.FloatField()
    level = models.PositiveIntegerField()
    type = models.CharField(max_length=5)
    msg = models.CharField(max_length=1000)

    class Meta:
        managed = False
        db_table = 'wp_wfstatus'


class WpWftrafficrates(models.Model):
    emin = models.PositiveIntegerField(db_column='eMin', primary_key=True)  # Field name made lowercase.
    ip = models.CharField(db_column='IP', max_length=16)  # Field name made lowercase.
    hittype = models.CharField(db_column='hitType', max_length=3)  # Field name made lowercase.
    hits = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'wp_wftrafficrates'
        unique_together = (('emin', 'ip', 'hittype'),)


class WpWpmailsmtpTasksMeta(models.Model):
    id = models.BigAutoField(primary_key=True)
    action = models.CharField(max_length=255)
    data = models.TextField()
    date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'wp_wpmailsmtp_tasks_meta'


class WpWysijaCampaign(models.Model):
    campaign_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=250, blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'wp_wysija_campaign'


class WpWysijaCampaignList(models.Model):
    list_id = models.PositiveIntegerField(primary_key=True)
    campaign_id = models.PositiveIntegerField()
    filter = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'wp_wysija_campaign_list'
        unique_together = (('list_id', 'campaign_id'),)


class WpWysijaCustomField(models.Model):
    name = models.TextField()
    type = models.TextField()
    required = models.IntegerField()
    settings = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'wp_wysija_custom_field'


class WpWysijaEmail(models.Model):
    email_id = models.AutoField(primary_key=True)
    campaign_id = models.PositiveIntegerField()
    subject = models.CharField(max_length=250)
    body = models.TextField(blank=True, null=True)
    created_at = models.PositiveIntegerField(blank=True, null=True)
    modified_at = models.PositiveIntegerField(blank=True, null=True)
    sent_at = models.PositiveIntegerField(blank=True, null=True)
    from_email = models.CharField(max_length=250, blank=True, null=True)
    from_name = models.CharField(max_length=250, blank=True, null=True)
    replyto_email = models.CharField(max_length=250, blank=True, null=True)
    replyto_name = models.CharField(max_length=250, blank=True, null=True)
    attachments = models.TextField(blank=True, null=True)
    status = models.IntegerField()
    type = models.IntegerField()
    number_sent = models.PositiveIntegerField()
    number_opened = models.PositiveIntegerField()
    number_clicked = models.PositiveIntegerField()
    number_unsub = models.PositiveIntegerField()
    number_bounce = models.PositiveIntegerField()
    number_forward = models.PositiveIntegerField()
    params = models.TextField(blank=True, null=True)
    wj_data = models.TextField(blank=True, null=True)
    wj_styles = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'wp_wysija_email'


class WpWysijaEmailUserStat(models.Model):
    user_id = models.PositiveIntegerField(primary_key=True)
    email_id = models.PositiveIntegerField()
    sent_at = models.PositiveIntegerField()
    opened_at = models.PositiveIntegerField(blank=True, null=True)
    status = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'wp_wysija_email_user_stat'
        unique_together = (('user_id', 'email_id'),)


class WpWysijaEmailUserUrl(models.Model):
    email_id = models.PositiveIntegerField()
    user_id = models.PositiveIntegerField(primary_key=True)
    url_id = models.PositiveIntegerField()
    clicked_at = models.PositiveIntegerField(blank=True, null=True)
    number_clicked = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'wp_wysija_email_user_url'
        unique_together = (('user_id', 'email_id', 'url_id'),)


class WpWysijaForm(models.Model):
    form_id = models.AutoField(primary_key=True)
    name = models.TextField(db_collation='utf8_bin', blank=True, null=True)
    data = models.TextField(db_collation='utf8_bin', blank=True, null=True)
    styles = models.TextField(db_collation='utf8_bin', blank=True, null=True)
    subscribed = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'wp_wysija_form'


class WpWysijaList(models.Model):
    list_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=250, blank=True, null=True)
    namekey = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    unsub_mail_id = models.PositiveIntegerField()
    welcome_mail_id = models.PositiveIntegerField()
    is_enabled = models.PositiveIntegerField()
    is_public = models.PositiveIntegerField()
    created_at = models.PositiveIntegerField(blank=True, null=True)
    ordering = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'wp_wysija_list'


class WpWysijaQueue(models.Model):
    user_id = models.PositiveIntegerField(primary_key=True)
    email_id = models.PositiveIntegerField()
    send_at = models.PositiveIntegerField()
    priority = models.IntegerField()
    number_try = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'wp_wysija_queue'
        unique_together = (('user_id', 'email_id'),)


class WpWysijaUrl(models.Model):
    url_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=250, blank=True, null=True)
    url = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'wp_wysija_url'


class WpWysijaUrlMail(models.Model):
    email_id = models.AutoField(primary_key=True)
    url_id = models.PositiveIntegerField()
    unique_clicked = models.PositiveIntegerField()
    total_clicked = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'wp_wysija_url_mail'
        unique_together = (('email_id', 'url_id'),)


class WpWysijaUser(models.Model):
    user_id = models.AutoField(primary_key=True)
    wpuser_id = models.PositiveIntegerField()
    email = models.CharField(unique=True, max_length=255)
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    ip = models.CharField(max_length=100)
    confirmed_ip = models.CharField(max_length=100)
    confirmed_at = models.PositiveIntegerField(blank=True, null=True)
    last_opened = models.PositiveIntegerField(blank=True, null=True)
    last_clicked = models.PositiveIntegerField(blank=True, null=True)
    keyuser = models.CharField(max_length=255)
    created_at = models.PositiveIntegerField(blank=True, null=True)
    status = models.IntegerField()
    domain = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'wp_wysija_user'


class WpWysijaUserField(models.Model):
    field_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=250, blank=True, null=True)
    column_name = models.CharField(max_length=250)
    type = models.PositiveIntegerField(blank=True, null=True)
    values = models.TextField(blank=True, null=True)
    default = models.CharField(max_length=250)
    is_required = models.PositiveIntegerField()
    error_message = models.CharField(max_length=250)

    class Meta:
        managed = False
        db_table = 'wp_wysija_user_field'


class WpWysijaUserHistory(models.Model):
    history_id = models.AutoField(primary_key=True)
    user_id = models.PositiveIntegerField()
    email_id = models.PositiveIntegerField(blank=True, null=True)
    type = models.CharField(max_length=250)
    details = models.TextField(blank=True, null=True)
    executed_at = models.PositiveIntegerField(blank=True, null=True)
    executed_by = models.PositiveIntegerField(blank=True, null=True)
    source = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'wp_wysija_user_history'


class WpWysijaUserList(models.Model):
    list_id = models.PositiveIntegerField(primary_key=True)
    user_id = models.PositiveIntegerField()
    sub_date = models.PositiveIntegerField(blank=True, null=True)
    unsub_date = models.PositiveIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'wp_wysija_user_list'
        unique_together = (('list_id', 'user_id'),)


class WpYoastIndexable(models.Model):
    permalink = models.TextField(blank=True, null=True)
    permalink_hash = models.CharField(max_length=40, blank=True, null=True)
    object_id = models.BigIntegerField(blank=True, null=True)
    object_type = models.CharField(max_length=32)
    object_sub_type = models.CharField(max_length=32, blank=True, null=True)
    author_id = models.BigIntegerField(blank=True, null=True)
    post_parent = models.BigIntegerField(blank=True, null=True)
    title = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    breadcrumb_title = models.TextField(blank=True, null=True)
    post_status = models.CharField(max_length=20, blank=True, null=True)
    is_public = models.IntegerField(blank=True, null=True)
    is_protected = models.IntegerField(blank=True, null=True)
    has_public_posts = models.IntegerField(blank=True, null=True)
    number_of_pages = models.PositiveIntegerField(blank=True, null=True)
    canonical = models.TextField(blank=True, null=True)
    primary_focus_keyword = models.CharField(max_length=191, blank=True, null=True)
    primary_focus_keyword_score = models.IntegerField(blank=True, null=True)
    readability_score = models.IntegerField(blank=True, null=True)
    is_cornerstone = models.IntegerField(blank=True, null=True)
    is_robots_noindex = models.IntegerField(blank=True, null=True)
    is_robots_nofollow = models.IntegerField(blank=True, null=True)
    is_robots_noarchive = models.IntegerField(blank=True, null=True)
    is_robots_noimageindex = models.IntegerField(blank=True, null=True)
    is_robots_nosnippet = models.IntegerField(blank=True, null=True)
    twitter_title = models.TextField(blank=True, null=True)
    twitter_image = models.TextField(blank=True, null=True)
    twitter_description = models.TextField(blank=True, null=True)
    twitter_image_id = models.CharField(max_length=191, blank=True, null=True)
    twitter_image_source = models.TextField(blank=True, null=True)
    open_graph_title = models.TextField(blank=True, null=True)
    open_graph_description = models.TextField(blank=True, null=True)
    open_graph_image = models.TextField(blank=True, null=True)
    open_graph_image_id = models.CharField(max_length=191, blank=True, null=True)
    open_graph_image_source = models.TextField(blank=True, null=True)
    open_graph_image_meta = models.TextField(blank=True, null=True)
    link_count = models.IntegerField(blank=True, null=True)
    incoming_link_count = models.IntegerField(blank=True, null=True)
    prominent_words_version = models.PositiveIntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField()
    blog_id = models.BigIntegerField()
    language = models.CharField(max_length=32, blank=True, null=True)
    region = models.CharField(max_length=32, blank=True, null=True)
    schema_page_type = models.CharField(max_length=64, blank=True, null=True)
    schema_article_type = models.CharField(max_length=64, blank=True, null=True)
    has_ancestors = models.IntegerField(blank=True, null=True)
    estimated_reading_time_minutes = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'wp_yoast_indexable'


class WpYoastIndexableHierarchy(models.Model):
    indexable_id = models.PositiveIntegerField(primary_key=True)
    ancestor_id = models.PositiveIntegerField()
    depth = models.PositiveIntegerField(blank=True, null=True)
    blog_id = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'wp_yoast_indexable_hierarchy'
        unique_together = (('indexable_id', 'ancestor_id'),)


class WpYoastMigrations(models.Model):
    version = models.CharField(unique=True, max_length=191, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'wp_yoast_migrations'


class WpYoastPrimaryTerm(models.Model):
    post_id = models.BigIntegerField(blank=True, null=True)
    term_id = models.BigIntegerField(blank=True, null=True)
    taxonomy = models.CharField(max_length=32)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField()
    blog_id = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'wp_yoast_primary_term'


class WpYoastSeoLinks(models.Model):
    id = models.BigAutoField(primary_key=True)
    url = models.CharField(max_length=255, blank=True, null=True)
    post_id = models.PositiveBigIntegerField(blank=True, null=True)
    target_post_id = models.PositiveBigIntegerField(blank=True, null=True)
    type = models.CharField(max_length=8, blank=True, null=True)
    indexable_id = models.PositiveIntegerField(blank=True, null=True)
    target_indexable_id = models.PositiveIntegerField(blank=True, null=True)
    height = models.PositiveIntegerField(blank=True, null=True)
    width = models.PositiveIntegerField(blank=True, null=True)
    size = models.PositiveIntegerField(blank=True, null=True)
    language = models.CharField(max_length=32, blank=True, null=True)
    region = models.CharField(max_length=32, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'wp_yoast_seo_links'
