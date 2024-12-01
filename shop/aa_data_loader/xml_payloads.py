# def add_category_payload(
#         id_parent: int,
#         active: bool,
#         name: str,
#         description: str,
#         link_rewrite: str
# ) -> str:
#     return f"""<prestashop xmlns:xlink="http://www.w3.org/1999/xlink">
# <category>
# <id>
# <![CDATA[{id}]]>
# </id>
# <id_parent>
# <![CDATA[{id_parent}]]>
# </id_parent>
# <active>
# <![CDATA[{active}]]>
# </active>
# <id_shop_default>
# <![CDATA[1]]>
# </id_shop_default>
# <is_root_category>
# <![CDATA[{is_root_category}]]>
# </is_root_category>
# <position>
# <![CDATA[{position}]]>
# </position>
# <name>
# <language id="1">
# <![CDATA[{name}]]>
# </language>
# </name>
# <link_rewrite>
# <language id="1">
# <![CDATA[{link_rewrite}]]>
# </language>
# </link_rewrite>
# <description>
# <language id="1">
# <![CDATA[{description}]]>
# </language>
# </description>
# <meta_title>
# <language id="1">
# <![CDATA[{meta_title}]]>
# </language>
# </meta_title>
# <meta_description>
# <language id="1">
# <![CDATA[{meta_description}]]>
# </language>
# </meta_description>
# <meta_keywords>
# <language id="1">
# <![CDATA[{meta_keywords}]]>
# </language>
# </meta_keywords>
# <associations>
# <categories>
# <category>
# <id>
# <![CDATA[{}]]>
# </id>
# </category>
# </categories>
# <products>
# <product>
# <id>
# <![CDATA[ ]]>
# </id>
# </product>
# </products>
# </associations>
# </category>
# </prestashop>"""


def add_product_payload(
        default_category_id: int,
        price: float,
        enabled: bool,
        name: str,
        url: str,
        description: str,
        short_description: str,
        category_id: int,
        state: int
) -> str:
    return f"""<prestashop xmlns:xlink="http://www.w3.org/1999/xlink">
                  <product>
                    <id_category_default><![CDATA[{default_category_id}]]></id_category_default>
                    <price><![CDATA[{price}]]></price>
                    <active><![CDATA[{1 if enabled else 0}]]></active> 
                    <name>
                      <language id="1"><![CDATA[{name}]]></language>
                    </name>
                    <link_rewrite>
                      <language id="1"><![CDATA[{url}]]></language>
                    </link_rewrite>
                    <description>
                      <language id="1"><![CDATA[{description}]]></language>
                    </description>
                    <description_short>
                      <language id="1"><![CDATA[{short_description}]]></language>
                    </description_short>
                    <state><![CDATA[{state}]]></state>
                    <associations>
                      <categories>
                        <category>
                          <id><![CDATA[{category_id}]]></id>
                        </category>
                      </categories>
                    </associations>
                  </product>
                </prestashop>
                """
    # jeżeli produkt ma być w kilku kategoriach to ten fragment dodaje następne kategorie
    # kiedy default-category jest tą główną
    # <associations>
    #     <categories>
    #       <category>
    #         <id><![CDATA[{category_id}]]></id>                              <!-- Category ID -->
    #       </category>
    #     </categories>
    #   </associations>

