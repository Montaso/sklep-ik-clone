def add_category_payload(
        id_parent: int,
        active: bool,
        name: str,
        description: str,
        link_rewrite: str
) -> str:
    return f"""<?xml version="1.0" encoding="UTF-8"?>
                <prestashop>
                    <category>
                        <id_parent><![CDATA[{id_parent}]]></id_parent>
                        <active><![CDATA[1]]></active>
                            <active><![CDATA[{active}]]></active>
                        <name>
                            <language id="1"><![CDATA[{name}]]></language>
                        </name>
                        <link_rewrite>
                            <language id="1"><![CDATA[{link_rewrite}]]></language>
                        </link_rewrite>
                        <description>
                            <language id="1">
                                <![CDATA[{description}]]>
                            </language>
                        </description>
                    </category>
                </prestashop>"""


def add_product_payload(
        default_category_id: int,
        price: float,
        enabled: bool,
        name: str,
        url: str,
        description: str,
        category_id: int,
        state: int,
        weight: int
) -> str:
    return f"""<prestashop xmlns:xlink="http://www.w3.org/1999/xlink">
                  <product>
                    <id_category_default><![CDATA[{default_category_id}]]></id_category_default>
                    <price><![CDATA[{price}]]></price>
                    <active><![CDATA[{1 if enabled else 0}]]></active> 
                    <available_for_order>1</available_for_order>
                    <weight><![CDATA[{weight}]]></weight>
                    <name>
                      <language id="1"><![CDATA[{name}]]></language>
                    </name>
                    <link_rewrite>
                      <language id="1"><![CDATA[{url}]]></language>
                    </link_rewrite>
                    <description>
                      <language id="1"><![CDATA[{description}]]></language>
                    </description>
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

