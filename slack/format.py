class SlackFormatter():
    # Already validated
    def notion_draft(self, values):
        obj = {}
        obj["attachments"] = [None] * len(values)

        for i in range(len(values)):
            color = None
            if values[i]['days'] < 7: 
                color="good"
            elif values[i]['days'] < 21:
                color="warning"
            else:
                color="danger"

            obj["attachments"][i] = {
                "fallback": "Drafts 알림",
                "title": values[i]['title'],
                "title_link": values[i]['url'],
                "text": "최종 수정한 지 *{0}일* 지났습니다.".format(values[i]['days']),
                "mrkdwn_in": ["text"],
                "color": color
            }

        obj['attachments'][0]['pretext'] =  "다음과 같은 미완성 Drafts들이 있습니다."

        return obj

