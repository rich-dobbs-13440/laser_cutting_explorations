<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
  <xsl:output method="xml" indent="yes" />

  <!-- Main template -->
  <xsl:template match="/">
    <svg xmlns="http://www.w3.org/2000/svg">
      <!-- Import and merge the contents of each file with corresponding properties -->
      <xsl:apply-templates select="document('spice_rack_cut.svg')" />
    </svg>
  </xsl:template>

</xsl:stylesheet>
