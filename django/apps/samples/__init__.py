from dbs.models import WpPosts, WpPostmeta
import datetime

"""
sample usage: in shell do this
source venv/bin/activate
cd project
python manage.py shell_plus

in shell plus:
> from apps.samples import get_latest_post
>  get_lastest_post()

"""


def get_latest_post():
	posts = WpPosts.objects.using("default").filter(
		post_status = 'publish'
	).order_by("-post_date")[:10]
	
	for item in posts:
		print(item.__dict__)


def migrate():

	trikinet_posts = WpPosts.objects.using("trikinet").filter(
		post_status = "publish",
		post_type = "post",
		post_date__date__range=["2020-12-01", "2020-12-31"]

	)

	for item in trikinet_posts:

		try:
			ds_posts = WpPosts.objects.using("default").get(
				post_name = item.post_name,
				post_type = 'post'
			)
		except WpPosts.DoesNotExist:

			ds_posts = None

		if ds_posts :

			try :

				thumbnail_id_trikinet = WpPostmeta.objects.using("trikinet").get(
					post_id = item.id,
					meta_key = '_thumbnail_id'
				)

			except WpPostmeta.DoesNotExist:

				thumbnail_id_trikinet = None

			if thumbnail_id_trikinet :

				thumbnail_src_trikinet = WpPostmeta.objects.using("trikinet").filter(
					post_id = thumbnail_id_trikinet.meta_value
				)

				try :
					attachment_trikinet = WpPosts.objects.using("trikinet").get(id=thumbnail_id_trikinet.meta_value, post_type='attachment', post_status='inherit')

				except WpPosts.DoesNotExist:

					attachment_trikinet = None


				if attachment_trikinet:

					featured_image_ds = WpPostmeta.objects.filter(post_id=ds_posts.id, meta_key="_thumbnail_id")
					featured_image_ds.delete()

					attachment_ds = WpPosts(
						post_author = attachment_trikinet.post_author,
						post_date = attachment_trikinet.post_date,
						post_date_gmt = attachment_trikinet.post_date_gmt,
						post_content= attachment_trikinet.post_content,
						post_title = attachment_trikinet.post_title,
						post_status = 'inherit' ,
						comment_status = 'open' ,
						ping_status = 'open' ,
						post_name = attachment_trikinet.post_name,
						post_modified = attachment_trikinet.post_modified,
						post_modified_gmt = attachment_trikinet.post_modified_gmt,
						post_parent = ds_posts.id,
						guid = attachment_trikinet.guid,
						menu_order = 0,
						post_type = 'attachment',
						post_mime_type = attachment_trikinet.post_mime_type,
						comment_count = 0
					)
					attachment_ds.save()

					thumbnail_id_ds = WpPostmeta(

						post_id = ds_posts.id,
						meta_key = '_thumbnail_id',
						meta_value = attachment_ds.pk ,
					)

					thumbnail_id_ds.save()

					for thumbnail_trikinet in thumbnail_src_trikinet:

						thumbnails = WpPostmeta(
							post_id = attachment_ds.pk,
							meta_key = thumbnail_trikinet.meta_key,
							meta_value = thumbnail_trikinet.meta_value
						)
						thumbnails.save()

				else :
					print("attachment trikinet " + item.post_name + " not found in trikinet")
					
			else :

				print("thumbnail id trikinet " + item.post_name + "not found in trikinet")


		else :

			print("post trikinet %s not found in dailysocial", item.post_name)






