<?php
/* Smarty version 3.1.48, created on 2024-11-27 19:26:49
  from '/var/www/html/themes/classic/templates/errors/restricted-country.tpl' */

/* @var Smarty_Internal_Template $_smarty_tpl */
if ($_smarty_tpl->_decodeProperties($_smarty_tpl, array (
  'version' => '3.1.48',
  'unifunc' => 'content_67476469ed48b6_75517965',
  'has_nocache_code' => false,
  'file_dependency' => 
  array (
    '1d32c0290e6cf857d0b58a4b3275948431f7b7f5' => 
    array (
      0 => '/var/www/html/themes/classic/templates/errors/restricted-country.tpl',
      1 => 1702485415,
      2 => 'file',
    ),
  ),
  'includes' => 
  array (
  ),
),false)) {
function content_67476469ed48b6_75517965 (Smarty_Internal_Template $_smarty_tpl) {
$_smarty_tpl->_loadInheritance();
$_smarty_tpl->inheritance->init($_smarty_tpl, true);
?>


<?php 
$_smarty_tpl->inheritance->instanceBlock($_smarty_tpl, 'Block_121683448367476469ed0d92_22587818', 'content');
?>

<?php $_smarty_tpl->inheritance->endChild($_smarty_tpl, 'layouts/layout-error.tpl');
}
/* {block 'page_title'} */
class Block_79338392367476469ed1d91_15795787 extends Smarty_Internal_Block
{
public function callBlock(Smarty_Internal_Template $_smarty_tpl) {
echo htmlspecialchars($_smarty_tpl->tpl_vars['shop']->value['name'], ENT_QUOTES, 'UTF-8');
}
}
/* {/block 'page_title'} */
/* {block 'page_header'} */
class Block_158128141267476469ed1ac6_51505739 extends Smarty_Internal_Block
{
public function callBlock(Smarty_Internal_Template $_smarty_tpl) {
?>

          <h1><?php 
$_smarty_tpl->inheritance->instanceBlock($_smarty_tpl, 'Block_79338392367476469ed1d91_15795787', 'page_title', $this->tplIndex);
?>
</h1>
        <?php
}
}
/* {/block 'page_header'} */
/* {block 'page_header_container'} */
class Block_1797641167476469ed11e5_56714615 extends Smarty_Internal_Block
{
public function callBlock(Smarty_Internal_Template $_smarty_tpl) {
?>

      <header class="page-header">
        <div class="logo"><img src="<?php echo htmlspecialchars($_smarty_tpl->tpl_vars['shop']->value['logo'], ENT_QUOTES, 'UTF-8');?>
" alt="logo" loading="lazy"></div>
        <?php 
$_smarty_tpl->inheritance->instanceBlock($_smarty_tpl, 'Block_158128141267476469ed1ac6_51505739', 'page_header', $this->tplIndex);
?>

      </header>
    <?php
}
}
/* {/block 'page_header_container'} */
/* {block 'page_content'} */
class Block_188929663167476469ed2ec5_30598514 extends Smarty_Internal_Block
{
public function callBlock(Smarty_Internal_Template $_smarty_tpl) {
?>

          <h2><?php echo call_user_func_array( $_smarty_tpl->smarty->registered_plugins[Smarty::PLUGIN_FUNCTION]['l'][0], array( array('s'=>'403 Forbidden','d'=>'Shop.Theme.Global'),$_smarty_tpl ) );?>
</h2>
          <p><?php echo call_user_func_array( $_smarty_tpl->smarty->registered_plugins[Smarty::PLUGIN_FUNCTION]['l'][0], array( array('s'=>'You cannot access this store from your country. We apologize for the inconvenience.','d'=>'Shop.Theme.Global'),$_smarty_tpl ) );?>
</p>
        <?php
}
}
/* {/block 'page_content'} */
/* {block 'page_content_container'} */
class Block_254945967476469ed2bd3_01847426 extends Smarty_Internal_Block
{
public function callBlock(Smarty_Internal_Template $_smarty_tpl) {
?>

      <section id="content" class="page-content page-restricted">
        <?php 
$_smarty_tpl->inheritance->instanceBlock($_smarty_tpl, 'Block_188929663167476469ed2ec5_30598514', 'page_content', $this->tplIndex);
?>

      </section>
    <?php
}
}
/* {/block 'page_content_container'} */
/* {block 'page_footer_container'} */
class Block_171897067567476469ed40e6_73170310 extends Smarty_Internal_Block
{
public function callBlock(Smarty_Internal_Template $_smarty_tpl) {
?>


    <?php
}
}
/* {/block 'page_footer_container'} */
/* {block 'content'} */
class Block_121683448367476469ed0d92_22587818 extends Smarty_Internal_Block
{
public $subBlocks = array (
  'content' => 
  array (
    0 => 'Block_121683448367476469ed0d92_22587818',
  ),
  'page_header_container' => 
  array (
    0 => 'Block_1797641167476469ed11e5_56714615',
  ),
  'page_header' => 
  array (
    0 => 'Block_158128141267476469ed1ac6_51505739',
  ),
  'page_title' => 
  array (
    0 => 'Block_79338392367476469ed1d91_15795787',
  ),
  'page_content_container' => 
  array (
    0 => 'Block_254945967476469ed2bd3_01847426',
  ),
  'page_content' => 
  array (
    0 => 'Block_188929663167476469ed2ec5_30598514',
  ),
  'page_footer_container' => 
  array (
    0 => 'Block_171897067567476469ed40e6_73170310',
  ),
);
public function callBlock(Smarty_Internal_Template $_smarty_tpl) {
?>


  <section id="main">

    <?php 
$_smarty_tpl->inheritance->instanceBlock($_smarty_tpl, 'Block_1797641167476469ed11e5_56714615', 'page_header_container', $this->tplIndex);
?>


    <?php 
$_smarty_tpl->inheritance->instanceBlock($_smarty_tpl, 'Block_254945967476469ed2bd3_01847426', 'page_content_container', $this->tplIndex);
?>


    <?php 
$_smarty_tpl->inheritance->instanceBlock($_smarty_tpl, 'Block_171897067567476469ed40e6_73170310', 'page_footer_container', $this->tplIndex);
?>


  </section>

<?php
}
}
/* {/block 'content'} */
}
