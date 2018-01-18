import leopard_soup
import frequency_analysis

dead_leopard = "./crispy kittens/ck_01-18-18-19-58-07.txt"
frequency_analysis.count_whiskers(dead_leopard)

raise SystemExit

url = "https://www.reddit.com/r/VideoGameReviews/comments/771lp2/switch_kamiko_55_a_five_dollar_hidden_gem_on_the/"

if leopard_soup.verify_spots(url):
    leopard_soup.cook_leopard(url)
else:
    raise SystemExit
