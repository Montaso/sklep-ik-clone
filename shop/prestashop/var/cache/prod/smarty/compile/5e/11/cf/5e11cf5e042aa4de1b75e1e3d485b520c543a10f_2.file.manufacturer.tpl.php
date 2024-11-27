<?php
/* Smarty version 3.1.48, created on 2024-11-27 19:26:31
  from '/var/www/html/themes/classic/templates/catalog/listing/manufacturer.tpl' */

/* @var Smarty_Internal_Template $_smarty_tpl */
if ($_smarty_tpl->_decodeProperties($_smarty_tpl, array (
  'version' => '3.1.48',
  'unifunc' => 'content_67476457dec197_67789399',
  'has_nocache_code' => false,
  'file_dependency' => 
  array (
    '5e11cf5e042aa4de1b75e1e3d485b520c543a10f' => 
    array (
      0 => '/var/www/html/themes/classic/templates/catalog/listing/manufacturer.tpl',
      1 => 1702485415,
      2 => 'file',
    ),
  ),
  'includes' => 
  array (
    'file:catalog/_partials/products.tpl' => 1,
  ),
),false)) {
function content_67476457dec197_67789399 (Smarty_Internal_Template $_smarty_tpl) {
$_smarty_tpl->_loadInheritance();
$_smarty_tpl->inheritance->init($_smarty_tpl, true);
?>


<?php 
$_smarty_tpl->inheritance->instanceBlock($_smarty_tpl, 'Block_766855267476457c35828_86832872', 'product_list_header');
?>


<?php 
$_smarty_tpl->inheritance->instanceBlock($_smarty_tpl, 'Block_110898522467476457d16e09_98599257', 'product_list');
?>

<?php $_smarty_tpl->inheritance->endChild($_smarty_tpl, 'catalog/listing/product-list.tpl');
}
/* {block 'product_list_header'} */
class Block_766855267476457c35828_86832872 extends Smarty_Internal_Block
{
public $subBlocks = array (
  'product_list_header' => 
  array (
    0 => 'Block_766855267476457c35828_86832872',
  ),
);
public function callBlock(Smarty_Internal_Template $_smarty_tpl) {
?>

  <h1><?php echo call_user_func_array( $_smarty_tpl->smarty->registered_plugins[Smarty::PLUGIN_FUNCTION]['l'][0], array( array('s'=>'List of products by brand %brand_name%','sprintf'=>array('%brand_name%'=>$_smarty_tpl->tpl_vars['manufacturer']->value['name']),'d'=>'Shop.Theme.Catalog'),$_smarty_tpl ) );?>
</h1>
  <div id="manufacturer-short_description"><?php echo $_smarty_tpl->tpl_vars['manufacturer']->value['short_description'];?>
</div>
  <div id="manufacturer-description"><?php echo $_smarty_tpl->tpl_vars['manufacturer']->value['description'];?>
</div>
<?php
}
}
/* {/block 'product_list_header'} */
/* {block 'product_list'} */
class Block_110898522467476457d16e09_98599257 extends Smarty_Internal_Block
{
public $subBlocks = array (
  'product_list' => 
  array (
    0 => 'Block_110898522467476457d16e09_98599257',
  ),
);
public function callBlock(Smarty_Internal_Template $_smarty_tpl) {
?>

  <?php $_smarty_tpl->_subTemplateRender('file:catalog/_partials/products.tpl', $_smarty_tpl->cache_id, $_smarty_tpl->compile_id, 0, $_smarty_tpl->cache_lifetime, array('listing'=>$_smarty_tpl->tpl_vars['listing']->value,'productClass'=>"col-xs-12 col-sm-6 col-xl-3"), 0, false);
}
}
/* {/block 'product_list'} */
}
