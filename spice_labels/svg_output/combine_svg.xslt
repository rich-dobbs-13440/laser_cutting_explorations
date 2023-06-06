<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
  <xsl:output method="xml" indent="yes" />

  <!-- Main template -->
  <xsl:template match="/">
    <svg xmlns="http://www.w3.org/2000/svg">
      <!-- Import and merge the contents of each file with corresponding properties -->
      <xsl:apply-templates select="document('spice_rack_cut.svg')" />
      <xsl:apply-templates select="document('spice_rack_heavy_etch.svg')" />
      <xsl:apply-templates select="document('spice_rack_light_etch.svg')" />
      <xsl:apply-templates select="document('spice_rack_medium_etch.svg')" />
      <xsl:apply-templates select="document('spice_rack_score.svg')" />
    </svg>
  </xsl:template>

  <!-- Copy template to merge contents -->
  <xsl:template match="*">
    <xsl:copy>
      <!-- Apply stroke, fill, and stroke-width values from corresponding properties file -->
      <xsl:apply-templates select="@*" />
      <xsl:apply-templates select="document(concat(document-uri(.), '.properties'))/*" />
      <xsl:apply-templates />
    </xsl:copy>
  </xsl:template>

  <!-- Apply stroke, fill, and stroke-width values -->
  <xsl:template match="path/@stroke">
    <xsl:attribute name="stroke">
      <xsl:value-of select="." />
    </xsl:attribute>
  </xsl:template>

  <xsl:template match="path/@fill">
    <xsl:attribute name="fill">
      <xsl:value-of select="." />
    </xsl:attribute>
  </xsl:template>

  <xsl:template match="path/@stroke-width">
    <xsl:attribute name="stroke-width">
      <xsl:value-of select="." />
    </xsl:attribute>
  </xsl:template>
</xsl:stylesheet>
